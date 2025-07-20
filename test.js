#separator:tab
#html:true
"<div id=""items"">
	<div id=""path""></div>
	<div id=""deck"">Info-math::Programing language::Python::Asynchronous File I/O</div>
	<div id=""front"">
		How read files with asynchronous?
	</div>
</div>
<script>
	deck = document.getElementById(""deck"");
	dName = deck.innerText.split(""::"")
	deck.innerHTML = dName[dName.length-1];
	document.getElementById(""path"").innerHTML = dName.join("" > "");
	function addTitle(id=false, title="""") {
		let el = document.getElementById(id);
		if (el.innerText) {
			let t = document.createElement(""div"");
			t.classList.add(""title"");
			t.innerHTML = title;

			let b = document.createElement(""div"");
			b.classList.add(""body"");
			b.innerHTML = el.innerHTML;

			while(el.firstChild) {
				el.removeChild(el.firstChild);
			}
			el.append(t, b);
		}
	}
	addTitle(""front"", ""Q. "");
</script>"	"<!-- Highlight.js stylesheet -->
<link rel=""stylesheet""
      href=""https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/styles/github-dark.min.css"">

<!-- Highlight.js core script -->
<script src=""https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/lib/highlight.min.js""></script>

<div id=""items"">
	<div id=""path""></div>
	<div id=""deck"">Info-math::Programing language::Python::Asynchronous File I/O</div>
	<div id=""front"">
		How read files with asynchronous?
	</div>
	<div id=""back-basic"">
		Use the <code>aiofiles</code> library with <code>async with</code> and <code>await</code> to read or write files without blocking the main event loop.
	</div>
	<div id=""back-code"">
		<center><table style=""color:#ccc; font-size: 15px;""><tbody><tr><td><div class=""highlight"" style=""background: #272822; padding-left:8px; padding-right:8px;""><pre style=""line-height: 125%;""><span style=""color: #FF4689"">import</span><span style=""color: #F8F8F2""> aiofiles</span>
<span style=""color: #FF4689"">import</span><span style=""color: #F8F8F2""> asyncio</span>

<span style=""color: #F8F8F2"">FILE_NAME</span> <span style=""color: #FF4689"">=</span> <span style=""color: #E6DB74"">'text.txt'</span>

<span style=""color: #66D9EF"">async</span> <span style=""color: #66D9EF"">def</span><span style=""color: #F8F8F2""> </span><span style=""color: #A6E22E"">write_file</span><span style=""color: #F8F8F2"">():</span>
    <span style=""color: #66D9EF"">async</span> <span style=""color: #66D9EF"">with</span> <span style=""color: #F8F8F2"">aiofiles</span><span style=""color: #FF4689"">.</span><span style=""color: #F8F8F2"">open(FILE_NAME,</span> <span style=""color: #F8F8F2"">mode</span><span style=""color: #FF4689"">=</span><span style=""color: #E6DB74"">'w'</span><span style=""color: #F8F8F2"">)</span> <span style=""color: #66D9EF"">as</span> <span style=""color: #F8F8F2"">f:</span>
        <span style=""color: #66D9EF"">for</span> <span style=""color: #F8F8F2"">i</span> <span style=""color: #FF4689"">in</span> <span style=""color: #F8F8F2"">range(</span><span style=""color: #AE81FF"">1</span><span style=""color: #F8F8F2"">,</span> <span style=""color: #AE81FF"">11</span><span style=""color: #F8F8F2"">):</span>
            <span style=""color: #66D9EF"">await</span> <span style=""color: #F8F8F2"">f</span><span style=""color: #FF4689"">.</span><span style=""color: #F8F8F2"">write(</span><span style=""color: #E6DB74"">f""line {</span><span style=""color: #F8F8F2"">i</span><span style=""color: #E6DB74"">}</span><span style=""color: #AE81FF"">\n</span><span style=""color: #E6DB74"">""</span><span style=""color: #F8F8F2"">)</span>

<span style=""color: #66D9EF"">async</span> <span style=""color: #66D9EF"">def</span><span style=""color: #F8F8F2""> </span><span style=""color: #A6E22E"">read_file</span><span style=""color: #F8F8F2"">():</span>
    <span style=""color: #66D9EF"">async</span> <span style=""color: #66D9EF"">with</span> <span style=""color: #F8F8F2"">aiofiles</span><span style=""color: #FF4689"">.</span><span style=""color: #F8F8F2"">open(FILE_NAME,</span> <span style=""color: #F8F8F2"">mode</span><span style=""color: #FF4689"">=</span><span style=""color: #E6DB74"">'r'</span><span style=""color: #F8F8F2"">)</span> <span style=""color: #66D9EF"">as</span> <span style=""color: #F8F8F2"">f:</span>
        <span style=""color: #F8F8F2"">contents</span> <span style=""color: #FF4689"">=</span> <span style=""color: #66D9EF"">await</span> <span style=""color: #F8F8F2"">f</span><span style=""color: #FF4689"">.</span><span style=""color: #F8F8F2"">read()</span>
        <span style=""color: #F8F8F2"">print(contents)</span>

<span style=""color: #66D9EF"">async</span> <span style=""color: #66D9EF"">def</span><span style=""color: #F8F8F2""> </span><span style=""color: #A6E22E"">main</span><span style=""color: #F8F8F2"">():</span>
    <span style=""color: #66D9EF"">await</span> <span style=""color: #F8F8F2"">write_file()</span>
    <span style=""color: #66D9EF"">await</span> <span style=""color: #F8F8F2"">read_file()</span>

<span style=""color: #F8F8F2"">asyncio</span><span style=""color: #FF4689"">.</span><span style=""color: #F8F8F2"">run(main())</span>
</pre></div>
</td></tr></tbody></table></center><br>
	</div>
	<div id=""additional-info""></div>
	<div id=""options""></div>
	<div id=""example""><center><table style=""color:#ccc; font-size: 15px;""><tbody><tr><td><div class=""highlight"" style=""background: #272822; padding-left:8px; padding-right:8px;""><pre style=""line-height: 125%;""><span style=""color: #66D9EF"">async</span> <span style=""color: #66D9EF"">def</span><span style=""color: #F8F8F2""> </span><span style=""color: #A6E22E"">read_file</span><span style=""color: #F8F8F2"">():</span>
    <span style=""color: #66D9EF"">async</span> <span style=""color: #66D9EF"">with</span> <span style=""color: #F8F8F2"">aiofiles</span><span style=""color: #FF4689"">.</span><span style=""color: #F8F8F2"">open(FILE_NAME,</span> <span style=""color: #F8F8F2"">mode</span><span style=""color: #FF4689"">=</span><span style=""color: #E6DB74"">'r'</span><span style=""color: #F8F8F2"">)</span> <span style=""color: #66D9EF"">as</span> <span style=""color: #F8F8F2"">f:</span>
        <span style=""color: #F8F8F2"">contents</span> <span style=""color: #FF4689"">=</span> <span style=""color: #66D9EF"">await</span> <span style=""color: #F8F8F2"">f</span><span style=""color: #FF4689"">.</span><span style=""color: #F8F8F2"">read()</span>
        <span style=""color: #F8F8F2"">print(contents)</span>
</pre></div>
</td></tr></tbody></table></center><br></div>
	<div id=""version""><strong>Python 3.7 or higher</strong></div>
</div>

<script>
	// Deck path logic
	const deck = document.getElementById(""deck"");
	const dName = deck.innerText.split(""::"")
	deck.innerHTML = dName[dName.length - 1];
	document.getElementById(""path"").innerHTML = dName.join("" > "");

	// Default version display
	const version = document.getElementById(""version"");
	version.innerHTML = version.innerHTML || "">= 3.7"";

	// Hide empty blocks
	[...document.getElementById(""items"").children].forEach(el => {
		if (!el.innerText.trim()) el.classList.add(""hidden"");
	});

	// Add title headings
	function addTitle(id, title) {
		const el = document.getElementById(id);
		if (el && el.innerText.trim()) {
			const t = document.createElement(""div"");
			t.classList.add(""title"");
			t.innerHTML = title;

			const b = document.createElement(""div"");
			b.classList.add(""body"");
			b.innerHTML = el.innerHTML;

			el.innerHTML = '';
			el.append(t, b);
		}
	}
	addTitle(""front"", ""Q. "");
	addTitle(""back-basic"", ""A. "");
	addTitle(""back-code"", ""A. "");
	addTitle(""options"", ""With Optional Params: "");
	addTitle(""example"", ""Example: "");
	addTitle(""additional-info"", ""&#9432;"");
	addTitle(""version"", ""Version: "");

	// Highlight all code blocks
	document.querySelectorAll('pre code').forEach((block) => {
		hljs.highlightElement(block);
	});
</script>
"
