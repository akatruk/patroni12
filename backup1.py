import subprocess, time, sys, subprocess, datetime, os, shutil, os.path

PWD="OPqUqWn0gzTMPB719uoYUS37+3R5kt43bzUlBaFL8nQ="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_cashback'
host = "M1K8SPLDB06"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="k476iThifFF63PvdfZEQW37ZWZ6jCvfAS4b4Vs5nGTA="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_api'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="9s60qM2R2AMrlKrA7adqMN7nfCtZmwK4xd1nzzgxgN0="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_auth'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="GTdnCkhjv++hyZ0dFieuoBAhl3AzvSOcCvNk16j7cGo="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_bank_history'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="HBHcG32ypku5VCkn9qUovFQg2sXWaXeYlqAhIXH6K9A="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_banking'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="XtmGoaiQpnbY3ZdXYJrJnQoV2kqOcZZiQ96UFRshEjI="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_banking_gateway'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="1ApKPDsKPcV11u2G4hyZNUz+ma5X4nuIzNzzsAIlwfs="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_config'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="N1j2YCpyWWoYk35hjm4jzC2ROsOPRvvPHljF9112Fnc="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_digitalbazaar'
host = "M1K8SPLDB07"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="se50ANLmXGtOcqgnmW/E8WfWLRTR13R2OZgb1dN7w1Y="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_cinema'
host = "M1K8SPLDB02"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="couDY1fJZT8CHLNhnr8UYePiQ1vBFfe+v2Z2tjlVmOA="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_cinema_demo'
host = "M1K8SPLDB02"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="oladN55EvVFtcjLwd1zlqbD3bxAjpfdnU86qLgBr8Rg="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_coupon'
host = "M1K8SPLDB03"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="NyWVeva96NL7nGyvDcxg1oqNvLZq9gqHIB/NgklcVeM="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_restaurants'
host = "M1K8SPLDB04"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="AqiOvgSZgjnfd9jkrwosTD8zqVgV1Dtg6YkF8asxWx8="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_message_processing'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="EbBGnC2tvqTvm3hslPCBBd09h74kRhbqhNhcHoLK3rM="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_notify'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="8UoopuFiCrsNXKqv8UrMql7nK4eHWjtKxBWbnTkB0rM="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_orders'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="DGlPHb9rTPnbGO5W8EPOhJjefAQNNEcBWPh53Fu95MA="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_payment'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="MyoT82grHNNjJkm51iwwBAZpW3noeYD724V6aBHY0MI="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_push_gateway'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="6iXum70RJv8Q6foaGJuKFwOsjgC6Xy3kcTLld5SnyTA="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_service_manager'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="mg2+H+K3nW4dLCUZ2bTz3N4zFbvzdPpsEKkhkNHpHUw="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_sms_gateway'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="jgLUSFteS17PJNWRlKgWEuCp8IXMDpmyZdXScVMmI+Y="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_user'
host = "M1K8SPLDB01"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="dUWmYe2Ulxlen4JKm5Eqfyn3WsXCxTiXRNuSYpXGCyA="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_yclients'
host = "M1K8SPLDB05"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="GU9B12MJUnvmoiej3u78337g4byfuNe93ealoIFf4bv="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_tanuki'
host = "M1K8SPLDB09"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

PWD="HJNFIEnubnjnev3d938h4gIn3SJJev9jNVUf98NBrjv="
x = datetime.datetime.now()
t = x.strftime("%d.%m.%y_%H.%M")
env = "prod/"
backup_dir= "/backup/"
fhole = backup_dir + env
db = 'lsp_fitmost'
host = "M1K8SPLDB08"
status,output = subprocess.getstatusoutput("PGPASSWORD=" + PWD + " /usr/pgsql-12/bin/pg_dump " + " -d " + db + " -U " + db + " -h " + host + " > " + fhole  + db + "_" + t + ".sql")
print(output)

# onlyfiles = next(os.walk(fhole))[2] #dir is your directory path as string
# print len(onlyfiles)
