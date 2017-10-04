import wget
for i in xrange(1670,3126):
    url= ('http://ddragon.leagueoflegends.com/cdn/7.18.1/img/profileicon/'+str(i)+'.png')
    filename = wget.download(url)
