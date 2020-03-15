<html>

<head>

</head>

<header>
<h2><b>Short Readme document about Headless Browsers</b></h2>
</header>

<body>
<p>Each Browser has own specific of the testing regarding automation.</p>

Firefox and Chrome do not have big difference in the automated testing:</p>
<ul>
<li><i>Geckodriver</i> is required for the <b>Firefox</b> and <i>chromedriver</i> is required for the <b>Chrome</b> browser.</li>
<li>Make sure that you have set the path of each driver. It is required as well.</li>
<li>You need to import <b>options</b> and add <b>--headless</b> argument:</li>
</ul>
<br>
<h4>How it looks for the Chrome browser...</h4>
<code>chrome_options = Options()</code>
<br>
<code>chrome_options.add_argument('--headless')</code>

<h4> and for the Firefox browser...</h4>
<code>firefox_options = Options()</code>
<br>
<code>firefox_options.add_argument('--headless')</code>
<br>


<br>
<h3>Advantages of using <b>headless</b> browser testing approach are:</h3>
<br>
<ol>
   <li>Better test performance compared to browser automation.</li>
   <li>Time consuming tests would run less as a result because headless browsers run faster.</li>
   <li>Opportunity to run tests on a system which doesn’t have a browser or for the app that does not have a GUI.</li>
   <li>Scrape website without a render of the full browser, you just need to compare some data, prices for instance.</li>
   <li>It could be a part of TDD that is very interesting and effective approach in web automation testing.</li>
</ol>

<h3>Popular Headless Browsers:</h3>
<ul>
   <li>Google <a href="https://developers.google.com/web/tools/puppeteer/">Puppeteer</a> - the Headless Browser Puppeteer is    a Node library. It gives you a high-level API to control headless Chrome or Chromium over the DevTools Protocol. It also      can also be tweaked to use full (non-headless) Chrome or Chromium</li>
   <li>Google Chrome since version 59</li>
   <li>Firefox versions 55 and 56</li>
   <li><a href="http://htmlunit.sourceforge.net/">HtmlUnit</a> is a “GUI-Less browser for Java programs”. It models HTML        documents and provides an API that allows you to invoke pages, fill out forms, click links, etc… just like you do in          your “normal” browser</li>
   <li><a href="https://splinter.readthedocs.io/en/latest/">Splinter</a> is a headless browser Python-centric option.  It's      open sourced and is used for testing web applications using Python.  For example, you can use it to automate browser          actions, such as visiting URLs and interacting with their items</li>
</ul>
</body>
</html>
