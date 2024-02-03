import discord
import chromedriver_autoinstaller
import json
from discord.ext import commands
from discord import Embed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

with open('config.json') as f:
    config = json.load(f)

intents = discord.Intents.all()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

chromedriver_autoinstaller.install()

driver = webdriver.Chrome(options=chrome_options)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='check')
async def check(ctx):
    try:
        checking_message = await ctx.send(content=ctx.author.mention, embed=Embed(title="Checking...", color=discord.Color.from_rgb(130, 0, 0)))
        driver.get("https://cas.tamu.edu/cas/login?service=https://applicant.tamu.edu/Account/Login&renew=true")
        driver.find_element(By.NAME, "username").send_keys(config["username"])
        driver.find_element(By.NAME, "password").send_keys(config["password"], Keys.RETURN)
        highlighted_text = await bot.loop.run_in_executor(None, lambda: WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".highlight"))).text)
        embed = Embed(title="Check Complete", description=highlighted_text, color=discord.Color.from_rgb(130, 0, 0))
        await checking_message.edit(content=ctx.author.mention, embed=embed)
        
    except Exception as e:
        print("Error:", e)
        await ctx.send("An error occurred. Please check the console for details.")

bot.run(config["botToken"])