
const puppeteer = require('puppeteer')

async function scrapePopulation(url) {
    document.getElementById("pop").innerHTML = "Here"
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url);

    const [el] = await page.$x('/html/body/div[3]/div[3]/div/div/div[2]/ul/li[1]/strong[2]');
    const txt = await el.getProperty('textContent');
    const population = await txt.jsonValue();

    document.getElementById("pop").innerHTML = {population}

    browser.close();
}
        
scrapePopulation('https://www.worldometers.info/world-population/us-population/')