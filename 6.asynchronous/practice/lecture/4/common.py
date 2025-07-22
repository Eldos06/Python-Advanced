import logging


log = logging.basicConfig(level=logging.INFO,
                          format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                          handlers=[
                              logging.FileHandler("file.log"),
                              logging.StreamHandler()
                          ],
                          datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(__name__)