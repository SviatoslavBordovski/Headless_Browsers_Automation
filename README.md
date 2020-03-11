<b>Short Readme document about Headless Browsers</b>

Each Browser has own specific of the testing regarding automation.

Firefox and Chrome do not have big difference in the automated testing.
<br>
1. <i>Geckodriver</i> is required for the <b>Firefox</b> and <i>chromedriver</i> is required for the <b>Chrome</b> browser.
2. Make sure that you have set the path of each driver. It is required as well.
3. You need to import <b>options</b> and add <b>--headless</b> argument:
<br>
   <code>chrome_options = Options()</code>
   <br>
   <code>chrome_options.add_argument("--headless")</code>
<br>
Advantages of using <b>headless</b> browser testing approach are:
<br>
<div>
<ol>
   <li>Better test performance compared to browser automation</li>
   <li>Time consuming tests would run less as a result</li>
   <li></li>
   <li></li>
   <li></li>
</ol>
</div>
