import asyncio
import aiohttp
import re
from bs4 import BeautifulSoup

async def page_get(session, url):#gets single page data
    async with session.get(url) as r: 
        s = r.status
        if s != 200: #handler for if data does not exist
            return False
        else:
          u= await r.read()
          return [url.split('/all/')[1], u]
    
async def get_all(session, urls): #allows for async data collection from all pages
    tasks = []
    for url in urls:
        task = asyncio.create_task(page_get(session,url)) 
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

def parse(results):
    outlist = []
    for html in results:
        if html != False:
            soup =BeautifulSoup(html[1], "html.parser")
            script = str([v for v in soup.find_all("script") if "imp_data" in v.text][0]) #finds player data
            scriptsp = script.split("\"platform\": null")[1]
            scriptsp1 = scriptsp.split("all")[1]
            scriptspl = scriptsp1.split("metadata")
            wins=[]#add extra stats to this area
            winperc=[]
            kills=[]
            kd=[]
            for f in scriptspl: #add extra stats to this area
                if "\"key\": \"Top1\"" in f:
                    g = (f.split("\"displayValue\": "))[1]
                    h = re.sub('[^A-Za-z0-9]+', '', g)
                    wins.append(int(h))
                elif "\"key\": \"WinRatio\"" in f:
                    g = (f.split("\"displayValue\": "))[1]
                    h = re.sub('[^A-Za-z0-9]+', '', g)
                    winperc.append(int(h))
                elif "\"key\": \"Kills\"" in f:
                    g = (f.split("\"displayValue\": "))[1]
                    h = re.sub('[^A-Za-z0-9]+', '', g)
                    kills.append(int(h))
                elif "\"key\": \"KD\"" in f:
                    g = (f.split("\"displayValue\": "))[1]
                    h = re.sub('[^A-Za-z0-9]+', '', g)

                    kd.append(int(h))
                
            outlist.append([html[0],wins[0],(winperc[0])/100,kills[0],(kd[0])/100])#add extra stats to this area
        else:
            continue
    return(outlist)

async def scrape(urls):
    async with aiohttp.ClientSession() as session:
        presults = []
        data = await get_all(session, urls)

        if data == [False]:#handler for if data does not exist
            return [False]
        else:
            presults=parse(data)
            return presults



#if __name__ == '__main__':
#    urls= ['https://fortnitetracker.com/profile/all/LazarLazar','https://fortnitetracker.com/profile/all/Gambit%20Toose']
#    
#    results = asyncio.run(scrape(urls))
#    print(results)