// Generated by Selenium IDE
import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.core.IsNot.not;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Alert;
import org.openqa.selenium.Keys;
import java.util.*;
import java.net.MalformedURLException;
import java.net.URL;
//headless mode
import org.openqa.selenium.chrome.ChromeOptions;

public class AddOwnerTest {
  static WebDriver driver; 
  //private or static??
  private Map<String, Object> vars;
  JavascriptExecutor js;
 
  @Before
  public void setUp() {
    print("Setup Add Owner Test");
    //Setting system properties of ChromeDriver
    System.setProperty("webdriver.chrome.driver", "/usr/local/bin/chromedriver");
    
    //Running test headless
    ChromeOptions chromeOptions = new ChromeOptions();
    chromeOptions.addArguments("--headless");

    driver = new ChromeDriver(chromeOptions);
    js = (JavascriptExecutor) driver;
    vars = new HashMap<String, Object>();
  }
  @After
  public void tearDown() {
    print("Selenium Test executed");
    driver.quit();
  }
  @Test
  public void addOwner() {
    print("Start Selenium Test");
    // Test name: Add_Owner
    // Step # | name | target | value | comment
    // 1 | open | /petclinics/ |  | 
    driver.get("http://40.114.35.24:8080/petclinics/");
    // 2 | setWindowSize | 1936x1056 |  | 
    driver.manage().window().setSize(new Dimension(1936, 1056));
    // 3 | click | css=li:nth-child(2) > a |  | 
    driver.findElement(By.cssSelector("li:nth-child(2) > a")).click();
    // 4 | click | linkText=Add Owner |  | 
    driver.findElement(By.linkText("Add Owner")).click();
    // 5 | click | id=firstName |  | 
    driver.findElement(By.id("firstName")).click();
    // 6 | type | id=firstName | John | 
    driver.findElement(By.id("firstName")).sendKeys("John");
    // 7 | type | id=lastName | Doe | 
    driver.findElement(By.id("lastName")).sendKeys("Doe");
    // 8 | type | id=address | Street X | 
    driver.findElement(By.id("address")).sendKeys("Street X");
    // 9 | type | id=city | City | 
    driver.findElement(By.id("city")).sendKeys("City");
    // 10 | type | id=telephone | 061234567 | 
    driver.findElement(By.id("telephone")).sendKeys("061234567");
    // 11 | click | id=add-owner-form |  | 
    driver.findElement(By.id("add-owner-form")).click();
    // 12 | click | css=.btn |  | 
    driver.findElement(By.cssSelector(".btn")).click();
    // 13 | click | linkText=Add New Pet |  | 
    driver.findElement(By.linkText("Add New Pet")).click();
    // 14 | click | id=name |  | 
    driver.findElement(By.id("name")).click();
    // 15 | type | id=name | pet1 | 
    driver.findElement(By.id("name")).sendKeys("pet1");
    // 16 | click | id=birthDate |  | 
    driver.findElement(By.id("birthDate")).click();
    // 17 | type | id=birthDate | 2020/12/11 | 
    driver.findElement(By.id("birthDate")).sendKeys("2020/12/11");
    // 18 | select | id=type | label=hamster | 
    {
      WebElement dropdown = driver.findElement(By.id("type"));
      dropdown.findElement(By.xpath("//option[. = 'hamster']")).click();
    }
    // 19 | click | css=option:nth-child(4) |  | 
    driver.findElement(By.cssSelector("option:nth-child(4)")).click();
    // 20 | click | css=.btn |  | 
    driver.findElement(By.cssSelector(".btn")).click();
    // 21 | close |  |  | 
    driver.close();
  }
}
