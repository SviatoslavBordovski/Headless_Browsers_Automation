<h2><b>Short Readme document about Headless Browsers</b></h2>

<p>Each Browser has own specific of the testing regarding automation.</p>

Firefox and Chrome do not have big difference in the automated testing:</p>
<br>
<ul>
<li><i>Geckodriver</i> is required for the <b>Firefox</b> and <i>chromedriver</i> is required for the <b>Chrome</b> browser.</li>
<li>Make sure that you have set the path of each driver. It is required as well.</li>
<li>You need to import <b>options</b> and add <b>--headless</b> argument:</li>
</ul>
<br>

<code>chrome_options = Options()</code>
<br>
<code>chrome_options.add_argument("--headless")</code>

<br>
<p>Advantages of using <b>headless</b> browser testing approach are:</p>
<br>
<ol>
   <li>Better test performance compared to browser automation</li>
   <li>Time consuming tests would run less as a result</li>
   <li>123</li>
   <li>123</li>
   <li>123</li>
</ol>
