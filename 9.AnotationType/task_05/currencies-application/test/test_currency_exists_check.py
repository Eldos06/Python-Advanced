from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, MagicMock, patch

from core.currency_exists_check import CurrencyExistsCheck


class TestExistsChecks(IsolatedAsyncioTestCase):

  def setUp(self):
    self.check = CurrencyExistsCheck()

  async def test_currency_exists_returns_true_for_cached_currency(self):
    self.check.cache_currencies = {"usd", "eur"}
    self.assertTrue(await self.check.currency_exists("usd"))

  async def test_currency_exists_returns_false_for_unknown_currency(self):
    self.check.cache_currencies = {"usd", "eur"}
    self.assertFalse(await self.check.currency_exists("xxx"))

  async def test_currency_exists_fetches_and_caches_when_empty(self):
    fake_currencies = {"usd": "US Dollar", "eur": "Euro"}
    with patch.object(
      CurrencyExistsCheck, "get_all_currencies", new=AsyncMock(return_value=fake_currencies)
    ) as mocked_fetch:
      result = await self.check.currency_exists("usd")

    self.assertTrue(result)
    self.assertEqual(self.check.cache_currencies, {"usd", "eur"})
    mocked_fetch.assert_awaited_once()

  async def test_currency_exists_does_not_refetch_when_cache_populated(self):
    self.check.cache_currencies = {"usd"}
    with patch.object(
      CurrencyExistsCheck, "get_all_currencies", new=AsyncMock()
    ) as mocked_fetch:
      await self.check.currency_exists("usd")

    mocked_fetch.assert_not_awaited()

  async def test_get_all_currencies_returns_parsed_json_from_api(self):
    fake_currencies = {"usd": "US Dollar", "eur": "Euro"}

    mock_response = MagicMock()
    mock_response.json = AsyncMock(return_value=fake_currencies)

    mock_get_cm = MagicMock()
    mock_get_cm.__aenter__ = AsyncMock(return_value=mock_response)
    mock_get_cm.__aexit__ = AsyncMock(return_value=None)

    mock_session = MagicMock()
    mock_session.get = MagicMock(return_value=mock_get_cm)

    mock_session_cm = MagicMock()
    mock_session_cm.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session_cm.__aexit__ = AsyncMock(return_value=None)

    with patch("core.currency_exists_check.aiohttp.ClientSession", return_value=mock_session_cm):
      result = await CurrencyExistsCheck.get_all_currencies()

    self.assertEqual(result, fake_currencies)
