

import aminofix
import os
import random
import sys
import urllib.request
import urllib.parse
import requests
import datetime
import json
import threading
import chistesESP as c
import time
import re
import string
import base64
import sqlite3
import youtube_dl
import wikipedia
from keep_alive import keep_alive
from hashlib import sha1
from io import BytesIO
from BotAmino import BotAmino
from gtts import gTTS
from random import uniform, choice, randint
from aminofix import socket
from os import path
from fancy_text import fancy
from google_trans_new import google_translator
from pathlib import Path
from contextlib import suppress
from BotAmino import path_download, path_sound
from flask import Flask
from threading import Thread
from youtube_dl import YoutubeDL
from lyrics_extractor import SongLyrics
from datetime import datetime
from joincomm import joincomm
from os import scandir, getcwd
from os.path import abspath
from json import load
from BotAmino import *
import time

#Declaraimporiables.
engineiddrev = "f834aa1c08b697c42"
apikeydrev = "AIzaSyDXor65H1jpxnFsQupGfm91oVio3rGHiEc"

extract_lyrics = SongLyrics(apikeydrev, engineiddrev)

keep_alive()  #==>Solo activar para hostear

print("Este bot esta cargando...")
#client = BotAmino()

fs = open("sids.txt", "r+")
sidd = (fs.read())
client = BotAmino(sid=sidd)

client.prefix = "!"
client.wait = 3
client.no_command_message = "Por lo general sigo ordenes, pero esa es... estupida"
client.spam_message = "¡Has esto, has aquello! Así es mi vida..."
client.activity = True
client.botId = '47c81c88-6203-4f13-b9d6-260e24d7e466'
wikipedia.set_lang("es")


# La estética base para cosas de bot
def esteticabase(t, conteudo, subtitulo=""):
    return f"""
[c]┏                    ───                      ┓ 
[C]──   Elena   ──
[C]✩✼　｡ﾟ･　　ﾟ･　☆　° ｡ 
[C] ❤️’• {t}
[C]         ╺╺╺╺╺╺╺╺(☕)
[C] — {subtitulo}
{conteudo}
[C]┗                                                  ┛    
        """


clienteamino = aminofix.Client()

versionbot = """Soy la versión más actualizda, ¡Por eso soy la mejor! bitchs. """

#Dueño


def tradlist(sub):
    sublist = []
    for elem in sub:
        try:
            sublist.append(
                client.get_from_code(
                    f"http://aminoapps.com/u/{elem}").objectId)
            continue
        except Exception:
            pass
        sublist.append(elem)
    return sublist


whitefile = 'whiteauthor.txt'
whitelist = []
try:
    with open(whitefile, 'r') as file:
        for whitelistmember in file.readlines():
            whitelist.append(whitelistmember.strip())
except FileNotFoundError:
    a = open(whitefile, "w")
    a.close()

whitelist = tradlist(whitelist)

files = {}
try:
    with open('mediaguardada.json') as f:
        files = json.load(f)
except Exception:
    with open('mediaguardada.json', 'w+') as f:
        json.dump(files, f, indent=2)


class Compiler():
    global api
    api = "https://wandbox.org/api/compile.json"

    def __init__(self, code):
        self.code = code

        self.data = {
            "code": self.code,
            "save": True,
        }

    #Python
    def pypy_head(self):
        self.data["compiler"] = "pypy-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["program_message"], r["status"], r["url"]

    #Julia
    def julia_head(self):
        self.data["compiler"] = "julia-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #C
    def gcc_head_c(self):
        self.data["compiler"] = "gcc-head-c"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #C++
    def gcc_head_pp(self):
        self.data["compiler"] = "gcc-head-pp"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    # C#
    def mono_head(self):
        self.data["compiler"] = "mono-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #Erlang
    def erlang_head(self):
        self.data["compiler"] = "erlang-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #Haskell
    def ghc_head(self):
        self.data["compiler"] = "ghc-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #D
    def dmd_head(self):
        self.data["compiler"] = "dmd-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #Java
    def openjdk_head(self):
        self.data["compiler"] = "openjdk-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #Rust
    def rust_head(self):
        self.data["compiler"] = "rust-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #Ruby
    def ruby_head(self):
        self.data["compiler"] = "ruby-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["program_message"], r["status"], r["url"]

    #Scala
    def scala_213x(self):
        self.data["compiler"] = "scala-2.13.x"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #NodeJS, JavaScript
    def nodejs_head(self):
        self.data["compiler"] = "nodejs-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["program_message"], r["status"], r["url"]

    #CoffeeScript
    def coffeescript_head(self):
        self.data["compiler"] = "coffeescript-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["program_message"], r["status"], r["url"]

    #Swift
    def swift_head(self):
        self.data["compiler"] = "swift-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #Perl
    def perl_head(self):
        self.data["compiler"] = "perl-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["program_message"], r["status"], r["url"]

    #PHP
    def php_head(self):
        self.data["compiler"] = "php-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["program_message"], r["status"], r["url"]

    #Lua
    def luajit_head(self):
        self.data["compiler"] = "luajit-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["program_message"], r["status"], r["url"]

    #SQL
    def sqlite_head(self):
        self.data["compiler"] = "sqlite-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["program_message"], r["status"], r["url"]

    #Pascal
    def fpc_head(self):
        self.data["compiler"] = "fpc-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #Vim
    def vim_head(self):
        self.data["compiler"] = "vim-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        return r["program_message"], r["status"], r["url"]

    #OCaml
    def ocaml_head(self):
        self.data["compiler"] = "ocaml-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["program_message"], r["status"], r["url"]

    #GO
    def go_head(self):
        self.data["compiler"] = "go-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #Lisp
    def sbcl_head(self):
        self.data["compiler"] = "sbcl-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["program_message"], r["status"], r["url"]

    #OpenSSL
    def openssl_head(self):
        self.data["compiler"] = "openssl-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["program_message"], r["status"], r["url"]

    # F#
    def fsharp_head(self):
        self.data["compiler"] = "fsharp-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    # .NET
    def dotnetcore_head(self):
        self.data["compiler"] = "dotnetcore-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]
        else:
            return r["compiler_message"], r["status"], r["url"]

    #R
    def r_head(self):
        self.data["compiler"] = "r-head"
        r = requests.post(api, data=json.dumps(self.data)).json()
        if str(r["status"]) == "0":
            return r["program_output"], r["status"], r["url"]


#     else:
#       return r["program_message"], r["status"], r["url"]


def is_it_me(data):
    if any(user in data.authorId for user in whitelist):
        return True
    data.subClient.send_message(
        chatId=data.chatId,
        message=
        "Tontito! No tienes acceso a mis comandos de Dueño. ૮₍ ˃̵͈᷄ . ˂̵͈᷅ ₎ა")
    return False


def gendevid(st: int = 50):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=st))
    dev = '01' + (MetaSpecial := sha1(ran.encode("utf-8"))).hexdigest() + sha1(
        bytes.fromhex('01') + MetaSpecial.digest() +
        base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()
    return dev


def url_like(url):
    link = requests.get(url)
    result = BytesIO(link.content)

    return result


def enviar_mensaje(cid, msg):
    acced = aminofix.SubClient(comId=cid, profile=client.profile)
    try:
        acced.send_message(**msg)
    except Exception:
        print("Hay un error.")


def botidok(data):
    return data.authorId in ('47c81c88-6203-4f13-b9d6-260e24d7e466',
                             '6d1d2b3e-6a85-4ab9-a268-1eb3dfa1ff3d')


def is_staff(data):
    return data.authorId in ("80a52450-e2eb-4654-98a2-31c559f43d80"
                             ) or data.subClient.is_in_staff(data.authorId)


def not_bot(data):
    return data.authorId != client.botId


@client.on_all(condition=not_bot)
def on_message(data) -> None:
    content = data.message
    mtype = data.info.message.type
    if mtype not in [0, 103] and content:
        data.subClient.send_message(
            data.chatId,
            message=f"""[C]Han borrado o escrito en un mensaje raro!
            
Mensaje = {data.message}""",
            embedTitle=f"{data.author}",
            embedContent="Presione Aqui",
            embedLink=f"ndc://user-profile/{data.authorId}",
            embedImage=url_like(data.authorIcon))


def dataDB():
    # Datos de la base de datos
    conn = sqlite3.connect('drevenzz.db')
    curs = conn.cursor()

    return conn, curs

@client.command("apodo")
def nick(data):
    conn, curs = dataDB()
    uid = data.authorId
    msg = data.message
    #msg = messageLower.split(" ")
    # Checkear si uid ya existe en la database
    b = curs.execute(f'SELECT * FROM drevdbs WHERE uid = "{uid}";').fetchall()
    # Si uid no existe en la db, agregarlo y reclamar premio
    if len(b) == 0:
        #reclamo = time.time()
        curs.execute(f"INSERT INTO drevdbs VALUES ('{uid}', '{msg}');")
        conn.commit()
        data.subClient.send_message(chatId=data.chatId,
                                    message="Apodo agregado al Usuario.")
    else:
        data.subClient.send_message(
            replyTo=data.messageId,
            chatId=data.chatId,
            message="El usuario ya se encuentra con un apodo.")

    conn.close()


bienvenidadreven = f"""[BC]─ ご꯭い :   𝐖𝐄𝐋𝐂𝐎𝐌𝐄 ! 🥢 𓂃⠀♡
[I]਼˟˛̥̽Bienvenid@ a la taberna del trueno.࿔᷏⋮᷆ᷓ
[Ic]਼˟˛̥̽Aquí podrás pasar un buen rato,
[Ci]siempre y cuando cumplas las normas del chat. ࿔᷏⋮᷆ᷓ
[CI]਼˟˛̥̽Accede a la descripción del chat para informarte más sobre estas.࿔᷏⋮᷆ᷓ
[Cb]¡ 𝕯𝘪𝘀𝖿𝗋ᴜ𝐭𝖺 !

[CuS]/ㅤ/ㅤㅤㅤ◜♡◝ㅤ  〔 ❆ 〕  ㅤ \ㅤ\

"""


@client.on_member_join_chat()
def on_group_member_join(data):
    conn, curs = dataDB()
    uid = data.authorId

    b = curs.execute(
        f'SELECT nick FROM drevdbs WHERE uid = "{uid}";').fetchall()

    numeromiembro = data.subClient.get_chat_thread(data.chatId).membersCount
    data.subClient.send_message(
        data.chatId,
        message=f"""{bienvenidadreven}[C]{data.author} eres bienvenido!""",
        mentionUserIds=[data.authorId],
        embedTitle=data.author,
        embedContent=f"Eres nuestro miembro #{numeromiembro}",
        embedImage=url_like(data.authorIcon),
        embedLink=f"ndc://user-profile/{data.authorId}")

    conn.close()


@client.command()
def aminojoin(data):
    resp = joincomm(client, f"{data.message}")

    if resp["error"] == "not found":
        data.subClient.send_message(
            data.chatId, message="No se ha encontrado la comunidad solicitada")
    if resp["error"] == "join error":
        data.subClient.send_message(data.chatId,
                                    message="Ocurrio un error al unirse")
    if resp["error"] == "ok":
        data.subClient.send_message(data.chatId, message="Hecho!")
        print("ID de la comunidad: %s" % resp["comId"])


@client.command("letra")
def lyrics(data):
    lyrics = extract_lyrics.get_lyrics(data.message)['lyrics']
    while len(lyrics) >= 2000:
        mes = lyrics[:2000]
        data.subClient.send_message(data.chatId, mes)
        lyrics = lyrics[2000:]
    data.subClient.send_message(data.chatId, lyrics)


@client.command("comus", is_it_me)
def comusids(data):
    chatId = data.chatId
    chatType = data.subClient.get_chat_thread(chatId).type
    subclients = data.subClient.sub_clients()
    if chatType == 0:
        data.subClient.send_message(data.chatId, message=name)


@client.command()
def didgen(data):
    didg = gendevid()
    didg2 = gendevid()
    didg3 = gendevid()
    didg4 = gendevid()
    didg5 = gendevid()
    didg6 = gendevid()
    didg7 = gendevid()
    didg8 = gendevid()
    didg9 = gendevid()
    did10 = gendevid()
    print(didg)
    print(didg2)
    print(didg3)
    print(didg4)
    print(didg5)
    print(didg6)
    print(didg7)
    print(didg8)
    print(didg9)
    print(did10)


@client.command("checkin")
def checkin(data):
    try:
        data.subClient.check_in()
        data.subClient.lottery()
        racha = data.subClient.get_user_checkins(
            data.subClient.profile.userId).consecutiveCheckInDays
        data.subClient.send_message(
            data.chatId,
            message=
            f"Check-In y Loteria Realizados! Tienes una Racha Consecutiva de {racha} Dias en tu Check-In"
        )
    except aminofix.lib.util.exceptions.AlreadyCheckedIn:
        racha = data.subClient.get_user_checkins(
            data.subClient.profile.userId).consecutiveCheckInDays
        data.subClient.send_message(
            data.chatId,
            message=
            f"Ya has Realizado Check-In en esta Comunidad y ya has participado en la loteria de Hoy! No olvides que tu Racha es de {racha} Dias."
        )
        pass


@client.command("lock", is_it_me)
def lock_command(args):
    if not args.message or args.message in args.subClient.locked_command or args.message not in client.commands_list(
    ) or args.message in ("lock", "unlock"):
        return
    try:
        args.message = args.message.lower().strip().split()
    except Exception:
        args.message = [args.message.lower().strip()]
    args.subClient.add_locked_command(args.message)
    args.subClient.send_message(args.chatId, "Locked command list updated")


@client.command("validdid")
def validedevice(data):
    try:
        valdid = data.subClient.check_device(deviceId=data.message)
        data.subClient.send_message(
            data.chatId, message=f"Tu DeviceId es valida, {valdid}.")
    except aminofix.lib.util.exceptions.InvalidDevice:
        data.subClient.send_message(data.chatId,
                                    message="Tu DeviceId es invalida.")
        pass


@client.command("stickerid", is_it_me)
def stickerid(data):
    if client.check(data, 'staff'):
        reply_message = data.info.json
        reply_messageId = reply_message["chatMessage"]['extensions'][
            'replyMessage']['messageId']
        data.subClient.send_message(
            chatId=data.chatId,
            message=reply_message["chatMessage"]["extensions"]["replyMessage"]
            ["extensions"]["sticker"]["stickerId"],
            replyTo=reply_messageId)


@client.command()
def sticker(data):
    stickerids = random.choice([
        "73bc3a43-9e2f-4273-8e1a-22cfa7c0593c",
        "10a84ea5-98ae-431c-a845-0b0f6cdf1dd5",
        "73bc3a43-9e2f-4273-8e1a-22cfa7c0593c",
        "b2caf12c-cef6-4ba4-a36b-eb8b603b0dd8"
    ])
    data.subClient.send_message(data.chatId, stickerId=stickerids)

@client.command("include")
def includeamino(data):
    codigo = data.message
    a = Compiler(codigo)
    b = a.r_head()
    for i in b:
        data.subClient.send_message(data.chatId, message=i)

#@client.command("sidchange")
#def sidchange(data):
    #try:
        #sit.drop()
        #time.sleep(1)
        #it={"sid":data.message}
        #sit.insert_one(it)
        #data.subClient.send_message(chatId=data.chatId,message="Sid changed")


#@client.command()
#def deviceid(data):
    #genids = gendevid()
    #data.subClient.send_message(data.chatId, message=genids)


@client.command()
def marco(data):
    data.subClient.subclient.apply_avatar_frame(avatarId=f"{data.message}",
                                                applyToAll=True)
    data.subClient.send_message(data.chatId,
                                message="Mi Marco ha sido cambiado")


@client.command()
def transid(data):
    trid = data.subClient.generate_transaction_id()
    data.subClient.send_message(data.chatId, message=trid)


@client.command("coin")
def monedero(data):
    balance = data.subClient.get_wallet_amount()
    data.subClient.send_message(
        data.chatId,
        message=f"Mis coins disponibles al momento son: {balance}.")


@client.command("shippname")
def names_Gen(data):
    delimitador = "- "  #Aqui puedes poner el delimitador que usas puede ser un * o un - entre otros, en este caso usamos un espacio
    texto = f"{data.message}"
    mensaje = texto.split(" ")

    nameOne = mensaje[0]
    nameTwo = mensaje[1]

    dataOne = {
        "a1": f"{str(nameOne)}",
        "a2": f"{str(nameTwo)}",
    }

    dataTwo = {
        "a1": f"{str(nameTwo)}",
        "a2": f"{str(nameOne)}",
    }

    postOne = requests.post("https://couplenamegenerator.com/combine",
                            data=dataOne)
    postTwo = requests.post("https://couplenamegenerator.com/combine",
                            data=dataTwo)

    respOne = postOne.json()
    respTwo = postTwo.json()

    data.subClient.send_message(data.chatId,
                                message=f"""[BCI]{nameOne} y {nameTwo}. 💗 
	
{respOne} 
{respTwo}""")


@client.command()
def iconusuario(data):
    id = client.get_from_code(data.message).objectId
    image = data.subClient.subclient.get_user_info(id).icon
    filename = image.split("/")[-1]
    filetype = image.split(".")[-1]
    if filetype != "gif":
        filetype = "image"
        urllib.request.urlretrieve(image, filename)
        with open(filename, 'rb') as fp:
            with suppress(Exception):
                data.subClient.send_message(data.chatId,
                                            file=fp,
                                            fileType=filetype)
                os.remove(filename)


@client.command("datos")
def datos(data):
    rep = data.subClient.get_user_info(data.authorId).reputation
    lvl = data.subClient.get_user_info(data.authorId).level
    crttime = data.subClient.get_user_info(data.authorId).createdTime
    followers = data.subClient.get_user_achievements(
        data.authorId).numberOfFollowersCount
    profilchange = data.subClient.get_user_info(data.authorId).modifiedTime
    commentz = data.subClient.get_user_info(data.authorId).commentsCount
    posts = data.subClient.get_user_achievements(
        data.authorId).numberOfPostsCreated
    followed = data.subClient.get_user_info(data.authorId).followingCount
    sysrole = data.subClient.get_user_info(data.authorId).role
    data.subClient.send_message(
        data.chatId,
        message=f"""[BCI]Datos del Usuario. ૮₍ ˃̵͈᷄ . ˂̵͈᷅ ₎ა

[C]Reputación = {rep}

[C]Nivel = {lvl}

[C]Creación = {crttime}

[C]Seguidores = {followers}

[C]Perfil modificado el = {profilchange}

[C]Comentarios = {commentz}

[C]Publicaciones = {posts}

[C]Seguidos = {followed}

[C]Rol = {sysrole}
""",
        embedTitle=data.author,
        embedContent="Datos del Usuario.",
        embedLink="https://drevenzz.com",
        embedImage=url_like(data.authorIcon))


@client.command("datosusuario")
def datosusuario(data):
    mention = data.subClient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for obj in mention:
        #iddd=client.get_from_code(data.message).objectId
        fotoo = data.subClient.subclient.get_user_info(obj).icon
        #obj = client.get_from_code(data.message).objectId
    nick = data.subClient.get_user_info(obj).nickname
    rep = data.subClient.get_user_info(obj).reputation
    lvl = data.subClient.get_user_info(obj).level
    crttime = data.subClient.get_user_info(obj).createdTime
    followers = data.subClient.get_user_achievements(
        obj).numberOfFollowersCount
    profilchange = data.subClient.get_user_info(obj).modifiedTime
    commentz = data.subClient.get_user_info(obj).commentsCount
    posts = data.subClient.get_user_achievements(obj).numberOfPostsCreated
    followed = data.subClient.get_user_info(obj).followingCount
    sysrole = data.subClient.get_user_info(obj).role
    data.subClient.send_message(data.chatId,
                                message=f"""[BCI]Datos del Usuario.

[C]Reputación = {rep}

[C]Nivel = {lvl}

[C]Creación = {crttime}

[C]Seguidores = {followers}

[C]Perfil modificado el = {profilchange}

[C]Comentarios = {commentz}

[C]Publicaciones = {posts}

[C]Seguidos = {followed}

[C]Rol = {sysrole}
""",
                                embedTitle=nick,
                                embedContent="Datos del Usuario.",
                                embedLink="https://drevenzz.com",
                                embedImage=url_like(fotoo))


#
@client.command("comentar")
def comment_user(data):
    params = data.message

    #search
    search = re.search("=", params)
    if search:
        tmp = re.split("=", params)
        user = data.subClient.search_users(data.comId, tmp[0])
        if not user: return
        message = {'message': tmp[1], 'userId': user.data.userId[0]}
    else:
        message = {'message': params, 'userId': data.userId}

    message_carga = {
        'chatId': data.chatId,
        'message': "[C]He dejado algo en tu muro, me agradezco de tu parte"
    }

    data.subClient.send_message(data.comId, message_carga)

    data.subClient.comment(message)


#


@client.command("staffpregunta")
def staffask(data):
    msg = data.message
    data.subClient.ask_amino_staff(message=f"""[BCI]Pregunta al Staff.
  
{msg}

[C]Mensaje enviado por = {data.author}  
[C]Soy Elena, fui enviada a hacerle esa pregunta al Staff. Espero que tengan bonitas tardes o noches."""
                                   )


#Juegos
@client.command("pvp")
def fight(data):
    # Argumentos
    args = data.message.split(" ")
    args.append(5)

    # Aquí sucede el juego en sí.
    score = [0, 0]
    r = 0
    winner = ""
    for loop in range(0, int(args[2])):
        r += 1
        score[0] = score[0] + randint(0, 1)
        score[1] = score[1] + randint(0, 1)

        # Se define el ganador de esta ronda
        if score[0] > score[1]:
            winner = args[0]
        elif score[0] < score[1]:
            winner = args[1]
        else:
            winner = "Nadie"
        data.subClient.send_message(
            data.chatId,
            esteticabase(
                "PvP", f"""
[cu]{args[0]} {score[0]} x {score[1]} {args[1]}
[c]
[c]{winner} está en ventaja!
        """, f"Round {r}"))
        sleep(1)
    data.subClient.send_message(data.chatId, f"{winner} ganó.")


@client.command()
def creadora(data):
    data.subClient.send_message(
        data.chatId,
        message="<$Mi diosa$>",
        mentionUserIds=["64ab67c5-14ff-4474-a759-29dd2e84db97"])

@client.command()
def reina(data):
    data.subClient.send_message(
        data.chatId,
        message="<$𝓜𝓲 𝓭𝓲𝓸𝓼𝓪$>",
        mentionUserIds=["ac7cbf46-b2df-4fc5-b930-83f97e6a7feb"])

@client.command()
def rey(data):
    data.subClient.send_message(
        data.chatId,
        message="<$Mi dios$>",
        mentionUserIds=["ae481803-98f7-4df0-92d7-fafe0e9311e7"])


@client.command()
def joinchats(data):
    data.subClient.join_all_chat()
    data.subClient.send_message(
        data.chatId,
        message="Listo, me he unido a todos los chats.. cuidenme.")


@client.command("chat")
def chatprueba(data):
    translator = google_translator()
    mesdata = data.message
    if mesdata:
        translateen = translator.translate(mesdata, lang_tgt='en')
        link = "https://api.deltaa.me/chatbot?message=" + translateen
        response = requests.get(link)
        json_data = json.loads(response.text)
        chatboten = json_data["message"]
        traduccion = translator.translate(chatboten, lang_tgt='es')
        data.subClient.send_message(data.chatId,
                                    message=f"{traduccion}",
                                    replyTo=data.messageId)
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="""Este comando es para charlar conmigo! 
Debes poner algo y te respondere.. :3""")


@client.command("version")
def versiondrevenzz(data):
    data.subClient.send_message(data.chatId, message=versionbot)


@client.command()
def idlink(data):
    id = client.get_from_code(f"{data.message}").objectId
    data.subClient.send_message(data.chatId,
                                message=f"La ID del Link es: {id}",
                                replyTo=data.messageId)


@client.command("rgbtxt")
def rgbtxtembed(data):
    datamess = data.message
    url = f'https://api.xteam.xyz/attp?file&text=' + datamess
    file = url_like(url)
    if datamess:
        data.subClient.send_message(chatId=data.chatId,
                                    embedContent="Toma para ti tu rgb.. >w<",
                                    embedTitle=f"{data.author}",
                                    file=file,
                                    fileType="gif")
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="""Este comando es para crear un banner! 
Debes poner algo para crear este banner.""")


@client.command("neontxt")
def neontxtembed(data):
    datamess = data.message
    url = f'https://api.xteam.xyz/textpro/neon?text={datamess}&APIKEY=0f5ab554f6404684'
    file = url_like(url)
    if datamess:
        data.subClient.send_message(chatId=data.chatId,
                                    embedContent="Toma para ti tu neon",
                                    embedTitle=f"{data.author}",
                                    file=file,
                                    fileType="image")
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="""Este comando es para crear un banner! 
Debes poner algo para crear este banner.""")


@client.command("snowtxt")
def snowtxtembed(data):
    datamess = data.message
    url = f'https://api.xteam.xyz/textpro/snowtext?text={datamess}&APIKEY=0f5ab554f6404684'
    file = url_like(url)
    if datamess:
        data.subClient.send_message(chatId=data.chatId,
                                    embedContent="Toma para ti tu snow.. >w<",
                                    embedTitle=f"{data.author}",
                                    file=file,
                                    fileType="image")
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="""Este comando es para crear un banner! 
Debes poner algo para crear este banner.""")


@client.command("gradienttxt")
def gradienttxtembed(data):
    datamess = data.message
    url = f'https://api.xteam.xyz/textpro/3dgradient?text={datamess}&APIKEY=0f5ab554f6404684'
    file = url_like(url)
    if datamess:
        data.subClient.send_message(chatId=data.chatId,
                                    embedContent="Toma para ti tu degradado",
                                    embedTitle=f"{data.author}",
                                    file=file,
                                    fileType="image")
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="""Este comando es para crear un banner! 
Debes poner algo para crear este banner.""")


@client.command("blackpinktxt")
def blackpinktxtembed(data):
    datamess = data.message
    url = f'https://api.xteam.xyz/textpro/blackpink?text={datamess}&APIKEY=0f5ab554f6404684'
    file = url_like(url)
    if datamess:
        data.subClient.send_message(
            chatId=data.chatId,
            embedContent="Toma para ti tu texto blackpink",
            embedTitle=f"{data.author}",
            file=file,
            fileType="image")
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="""Este comando es para crear un banner! 
Debes poner algo para crear este banner.""")


@client.command("summtxt")
def summtxtembed(data):
    datamess = data.message
    url = f'https://api.xteam.xyz/textpro/summerysandwriting?text={datamess}&APIKEY=0f5ab554f6404684'
    file = url_like(url)
    if datamess:
        data.subClient.send_message(chatId=data.chatId,
                                    embedContent="Toma para ti.. >w<",
                                    embedTitle=f"{data.author}",
                                    file=file,
                                    fileType="image")
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="""Este comando es para crear un banner! 
Debes poner algo para crear este banner.""")


@client.command("lolice")
def csgobannerembed(data):
    datamess = data.message
    url = f'https://some-random-api.ml/canvas/lolice?avatar={data.info.message.author.icon}'
    file = url_like(url)
    if datamess:
        data.subClient.send_message(
            chatId=data.chatId,
            embedContent="Toma este banner de CSGO para ti",
            embedTitle=f"{data.author}",
            file=file,
            fileType="image")
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="""Este comando es para crear un banner! 
Debes poner algo para crear este banner.""")


@client.command("harrypotter")
def hpbannerembed(data):
    datamess = data.message
    url = f'https://api.xteam.xyz/photooxy/harrypotter?text={datamess}&APIKEY=0f5ab554f6404684'
    file = url_like(url)
    if datamess:
        data.subClient.send_message(
            chatId=data.chatId,
            embedContent="Toma este banner de HP para ti",
            embedTitle=f"{data.author}",
            file=file,
            fileType="image")
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="""Este comando es para crear un banner! 
Debes poner algo para crear este banner.""")


@client.command("pokemon")
def pokemonbannerembed(data):
    datamess = data.message
    url = f'https://api.xteam.xyz/photooxy/pokemon?text={datamess}&APIKEY=0f5ab554f6404684'
    file = url_like(url)
    if datamess:
        data.subClient.send_message(
            chatId=data.chatId,
            embedContent="Toma este banner de Pokemon para ti",
            embedTitle=f"{data.author}",
            file=file,
            fileType="image")
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="""Este comando es para crear un banner! 
Debes poner algo para crear este banner.""")


@client.command("libreta")
def libretatxtembed(data):
    datamess = data.message
    url = f'https://api.xteam.xyz/magernulis6?text={datamess}&APIKEY=0f5ab554f6404684'
    file = url_like(url)
    if datamess:
        data.subClient.send_message(chatId=data.chatId,
                                    embedContent="Ha apuntado en su libreta",
                                    embedTitle=f"{data.author}",
                                    file=file,
                                    fileType="image")
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="""Este comando es para crear una libreta! 
Debes poner algo para escribir en tu libreta""")


@client.command("base64txt")
def encodebase64(data):
    mesdata = data.message
    link = f"https://api.xteam.xyz/encrypt/b64enc?text={mesdata}&APIKEY=0f5ab554f6404684"
    response = requests.get(link)
    json_data = json.loads(response.text)
    encodebase = json_data["result"]

    data.subClient.send_message(data.chatId,
                                message=f"{encodebase}",
                                replyTo=data.messageId)


@client.command("decodebase64")
def decodebase64(data):
    mesdata = data.message
    link = f"https://api.xteam.xyz/encrypt/b64dec?text={mesdata}&APIKEY=0f5ab554f6404684"
    response = requests.get(link)
    json_data = json.loads(response.text)
    decodebase = json_data["result"]

    data.subClient.send_message(data.chatId,
                                message=f"{decodebase}",
                                replyTo=data.messageId)


@client.command("suicidio")
def killembed(data):
    url = f'https://some-random-api.ml/canvas/wasted/?avatar={data.info.message.author.icon}'
    file = url_like(url)

    data.subClient.send_message(chatId=data.chatId,
                                embedContent="se ha suicidado",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("loli")
def lolipolice(data):
    url = f'https://some-random-api.ml/canvas/lolice/?avatar={data.info.message.author.icon}'
    file = url_like(url)

    data.subClient.send_message(chatId=data.chatId,
                                embedContent="Cara de Loli",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")

@client.command("gay")
def gay(data):
    url = f'https://some-random-api.ml/canvas/gay/?avatar={data.info.message.author.icon}'
    file = url_like(url)
    gay = random.choice([
        "Tiene un 35% brad pit ta lindo",
        "Tiene un 75% Eres mas gay que tu tio",
        "Tiene un 99% Damn dude, que gay",
        "Tiene un 49% mitad mitad",
        "Tiene un 101%, jamas vi alguien tan gay",
        "Tiene un 20% not bad",
        "Tiene un 0% macho alfa"
    ])
    data.subClient.send_message(chatId=data.chatId, 
                                embedContent=f"{gay}",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")  

@client.command("koala")
def perro(data):
    response = requests.get('https://some-random-api.ml/img/koala')
    json_data = json.loads(response.text)
    url = json_data['link']
    file = url_like(url)

    data.subClient.send_message(
        chatId=data.chatId,
        embedContent=f"Toma tu Koala hermoso {data.message}.. >//<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="image") 

@client.command("carcel")
def carcel(data):
    url = f'https://some-random-api.ml/canvas/jail/?avatar={data.info.message.author.icon}'
    file = url_like(url)
    carcel = random.choice([
        "Fue a la carcel por puto jajaja"
    ])
    data.subClient.send_message(chatId=data.chatId, 
                                embedContent=f"{carcel}",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("pixel")
def pixelate(data):
    url = f'https://some-random-api.ml/canvas/pixelate/?avatar={data.info.message.author.icon}'
    file = url_like(url)

    data.subClient.send_message(chatId=data.chatId,
                                embedContent="Pixelate .. >.<",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("bts")
def bts(data):
    url = f"https://api.xteam.xyz/randomimage/bts?APIKEY=87a1e51c20b50871"
    file = url_like(url)
    data.subClient.send_message(chatId=data.chatId,
                                embedContent="Toma tu imagen sobre bts...",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("wallpaperpc")
def wallpaperpc(data):
    url = f"https://api.xteam.xyz/randomimage/wallpaper?APIKEY=87a1e51c20b50871"
    file = url_like(url)
    data.subClient.send_message(chatId=data.chatId,
                                embedContent="Toma tu wallpaper para pc...",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("wallpapermovil")
def wallpapermovil(data):
    url = f"https://api.xteam.xyz/randomimage/wpmobile?APIKEY=87a1e51c20b50871"
    file = url_like(url)
    data.subClient.send_message(chatId=data.chatId,
                                embedContent="Toma tu wallpaper para movil...",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("neko")
def neko(data):
    url = f"https://api.xteam.xyz/randomimage/sfwneko?APIKEY=87a1e51c20b50871"
    file = url_like(url)
    data.subClient.send_message(chatId=data.chatId,
                                embedContent="Toma tu neko kawaii",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("jahy")
def jahy(data):
    url = f"https://api.xteam.xyz/randomimage/jahy?APIKEY=87a1e51c20b50871"
    file = url_like(url)
    data.subClient.send_message(chatId=data.chatId,
                                embedContent="Toma tu imagen de Jahy Sama...",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("perro")
def perro(data):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = json.loads(response.text)
    url = json_data['link']
    file = url_like(url)

    data.subClient.send_message(
        chatId=data.chatId,
        embedContent=f"Toma tu Perrito {data.message}.. >//<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="image")


@client.command("gato")
def gato(data):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)
    url = json_data['link']
    file = url_like(url)

    data.subClient.send_message(chatId=data.chatId,
                                embedContent=f"Toma tu Gatito {data.message}",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("zorro")
def zorro(data):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)
    url = json_data['link']
    file = url_like(url)

    data.subClient.send_message(chatId=data.chatId,
                                embedContent=f"Toma tu Zorrito {data.message}",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("simp")
def simpcard(data):
    url = f"https://some-random-api.ml/canvas/simpcard/?avatar={data.info.message.author.icon}"
    file = url_like(url)

    data.subClient.send_message(chatId=data.chatId,
                                embedContent="Obtuvo su tarjeta de simp",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("horny")
def simpcard(data):
    url = f"https://some-random-api.ml/canvas/horny/?avatar={data.info.message.author.icon}"
    file = url_like(url)

    data.subClient.send_message(chatId=data.chatId,
                                embedContent="Obtuvo una tarjeta muy horny..",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("selfie")
def selfieembed(data):
    url = f'{data.info.message.author.icon}'
    file = url_like(url)

    data.subClient.send_message(chatId=data.chatId,
                                embedContent="se ha tomado una selfie..",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="image")


@client.command("pat")
def patpatembed(data):
    response = requests.get('https://some-random-api.ml/animu/pat')
    json_data = json.loads(response.text)
    url = json_data['link']
    file = url_like(url)

    data.subClient.send_message(
        chatId=data.chatId,
        embedContent=f"le ha dado un pat en la cabeza a {data.message}",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("guiño")
def guiñopatembed(data):
    response = requests.get('https://some-random-api.ml/animu/wink')
    json_data = json.loads(response.text)
    url = json_data['link']
    file = url_like(url)

    data.subClient.send_message(
        chatId=data.chatId,
        embedContent=f"le ha dado un guiño a {data.message}",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


#

#


@client.command("coanfi", is_it_me)
def cohost(data):
    mention = data.subClient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    data.subClient.send_message(data.chatId, message="¿Qué crees? Soy coa")
    data.subClient.edit_chat(data.chatId, coHosts=mention)


@client.command("apagar", is_it_me)
def stop(args):
    args.subClient.send_message(
        args.chatId,
        "Me gustaría decir que no estoy cansado, pero eso sería una mentirilla"
    )
    os.execv(sys.executable, ["None", "None"])


@client.command("name", is_it_me)
def name(data):
    data.subClient.subclient.edit_profile(nickname=data.message)
    data.subClient.send_message(
        chatId=data.chatId,
        message=f"Mi nombre ha sido cambiado a {data.message}",
        replyTo=data.messageId)


@client.command("host", is_it_me)
def host(data):
    data.subClient.subclient.transfer_host(chatId=data.chatId,
                                           userIds=data.authorId)
    data.subClient.send_message(chatId=data.chatId, message="Host!")


@client.command("menciona")
def mention(args):
    try:
        size = int(args.message.strip().split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        size = 1

    val = args.subClient.get_user_id(args.message)
    if not val:
        args.subClient.send_message(
            chatId=args.chatId,
            message=
            "¿Seguro que lo escribiste bien? Usa los ojos para ver y dedos para escribir"
        )
        return

    if size > 5:
        size = 5

    if val:
        for _ in range(size):
            with suppress(Exception):
                args.subClient.send_message(chatId=args.chatId,
                                            message=f"‎‏‎‏@{val[0]}‬‭",
                                            mentionUserIds=[val[1]])


@client.command("bloquear", is_it_me)
def bloquear(data):
    mention = data.subClient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        data.subClient.subclient.block(userId=str(user))
        data.subClient.send_message(data.chatId,
                                    message="Ese malnacido ha sido bloqueado")


@client.command("desbloquear", is_it_me)
def desbloquear(data):
    mention = data.subClient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        data.subClient.subclient.unblock(userId=str(user))
        data.subClient.send_message(data.chatId,
                                    message="Listo, ha sido desbloqueado")


@client.command("comenta")
def comenta(data):
    mention = data.subClient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        data.subClient.comment(message=f"{data.message}", userId=str(user))
        data.subClient.send_message(
            chatId=data.chatId,
            message=
            f"{data.author} Observame comentar hasta allá {data.message}")


@client.command("clear", is_it_me)
def clear(args):
    if client.check(args, 'staff') and client.check(args, 'staff',
                                                    client.botId):
        size = 1
        args.subClient.delete_message(args.chatId,
                                      args.messageId,
                                      asStaff=True,
                                      reason="Clear")

        if size > 100:
            size = 100

        messages = args.subClient.get_chat_messages(chatId=args.chatId,
                                                    size=size).messageId

        for message in messages:
            with suppress(Exception):
                args.subClient.delete_message(args.chatId,
                                              message,
                                              asStaff=True)


@client.command("bienvenida", is_it_me)
def welcome_channel(args):
    if client.check(args, 'staff'):
        args.subClient.set_welcome_chat(args.chatId)
        args.subClient.send_message(args.chatId,
                                    "Mi bienvenida de Chat ha sido cambiada")


@client.command("unwelcome", is_it_me)
def unwelcome_channel(args):
    if client.check(args, 'staff'):
        args.subClient.unset_welcome_chat()
        args.subClient.send_message(args.chatId,
                                    "Se ha quitado la bienvenida de chat")


@client.command("aceptar")
def accept(args):
    if client.check(args, 'staff'):
        if args.subClient.accept_role("host", args.chatId):
            args.subClient.send_message(args.chatId, "Listo, estoy mejorado")
            return
        val = args.subClient.get_notices(start=0, size=25)
        for elem in val:
            print(elem["title"])
        ans = None
        res = None

        for elem in val:
            if 'become' in elem['title'] or "host" in elem['title']:
                res = elem['noticeId']
            if res:
                ans = args.subClient.accept_role(res)
            if ans:
                args.subClient.send_message(
                    args.chatId,
                    "He sido ascendido de puesto! Ahora soy mas poderoso que tu."
                )
                return
        else:
            args.subClient.send_message(args.chatId,
                                        "Ha ocurrido un error! :(")


@client.command("bienvenidamuro", is_staff)
def welcome(data):
    datamess = data.message
    if datamess:
        data.subClient.set_welcome_message(data.message)
        data.subClient.send_message(
            data.chatId,
            message=
            "Mi bienvenida de muro, ha sido activada y cambiada con lo que me han puesto"
        )
    else:
        data.subClient.send_message(
            data.chatId,
            message="""Con este comando puedes ponerme una bienvenida de muro!
Dare bienvenida a cada nuevo usuario en su muro, para esto usa el mismo comando poniendo la bienvenida que quieras que tenga en la comunidad!"""
        )


@client.command("reiniciar", is_it_me)
def reboot(args):
    sys.argv
    sys.executable
    args.subClient.send_message(
        args.chatId,
        "Denme solo 10 segundos ahora vuelvo, Pero antes de reiniciarme TODOS PUTOS"
    )
    os.execv(sys.executable, ["Python"] + sys.argv)


@client.command("id")
def idinfo(data):
    data.subClient.send_message(
        data.chatId,
        message=f"""{data.author} te conseguí la siguiente información, de nada
  
  Tu UserID: {data.authorId}
  Comunidad: {data.comId}
  ChatId: {data.chatId}""")


@client.command("disclaimer")
def disclaimerinfo(data):
    data.subClient.send_message(data.chatId,
                                message="""[C]Terminos y Condiciones del Bot
  
[C]Si usted invita/entra al bot a un chat, esta advertido que el dueño del bot puede revisar estos chats.

[C]Siguiendo lo anterior, la cuenta del bot es de su dueño y el puede disponer de ella libremente.

[C]Esta advertido a la hora de usarme y si no acepta estos terminos y condiciones.. no me uses. ₍ᐢ. .ᐢ₎""",
                                replyTo=data.messageId)


@client.command("terminosuser")
def terminosuser(data):
    data.subClient.send_message(
        data.chatId,
        message="""[C]Terminos y Condiciones del Usuario
  
[C]El bot puede almacenar, texto, imágenes y otras características, para su correcto uso. 

[C]Siguiendo lo anterior, el bot puede disponer de ella libremente y/o en caso sea necesario.

[C]El usuario acepta que el contenido es de uso libre, por lo mismo anteriormente. 
                              
[C]Esta advertido a la hora de usarme y si no acepta estos terminos y condiciones.. no me uses. ₍ᐢ. .ᐢ₎""",
        replyTo=data.messageId)


@client.command("bio", is_it_me)
def bio(data):
    data.subClient.subclient.edit_profile(content=data.message)
    data.subClient.send_message(
        chatId=data.chatId,
        message=f"Mi biografia ha sido cambiada, soy más guapa",
        replyTo=data.messageId)


@client.command("joinchat")
def join(data):
    val = data.subClient.join_chatroom(data.message, data.chatId)
    if val or val == "":
        data.subClient.send_message(
            data.chatId,
            f""" {data.author} me ha unido al siguiente chat: {val}
        
Estaba disfrutando de mi descanso... aunque a nadie le importe""".strip())
    else:
        data.subClient.send_message(
            data.chatId,
            "No me he podido unir al chat, ha ocurrido un error. Estoy muy triste de no poder estar en ese chat... Mentira, no me importa"
        )


@client.command("leavechat", is_it_me)
def leave(data):
    if data.message:
        chat_ide = data.subClient.get_chat_id(data.message)
        if chat_ide:
            data.chatId = chat_ide
    data.subClient.send_message(
        chatId=data.chatId,
        message="Cuando quieran que regrese, saben como hacerlo")
    data.subClient.leave_chat(data.chatId)


@client.command("view", is_it_me)
def Vmode(data):
    id = data.subClient.subclient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
        try:
            data.subClient.subclient.edit_chat(chatId=chat, viewOnly=True)
        except:
            pass


@client.command("descripcion", is_it_me)
def descripcionchat(data):
    id = data.subClient.subclient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
        try:
            data.subClient.subclient.edit_chat(chatId=chat,
                                               content=data.message)
            data.subClient.send_message(
                chatId=data.chatId, message="Descripcion del Chat cambiada")
        except:
            pass


@client.command("anuncio", is_it_me)
def anuncio(data):
    id = data.subClient.subclient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
        try:
            data.subClient.subclient.edit_chat(chatId=chat,
                                               announcement=data.message)
            data.subClient.send_message(chatId=data.chatId,
                                        message="Anuncio agregado")
        except:
            pass


@client.command("pinanuncio", is_it_me)
def pinanuncio(data):
    id = data.subClient.subclient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
        try:
            data.subClient.subclient.edit_chat(chatId=chat,
                                               pinAnnouncement=True)
            data.subClient.send_message(chatId=data.chatId,
                                        message="Anuncio destacado")
        except:
            pass


@client.command("titlechat", is_it_me)
def tittlechat(data):
    id = data.subClient.subclient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
        try:
            data.subClient.subclient.edit_chat(chatId=chat, title=data.message)
            data.subClient.send_message(chatId=data.chatId,
                                        message="Titulo agregado")
        except:
            pass


@client.command("unview", is_it_me)
def unvmode(data):
    id = data.subClient.subclient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
        try:
            data.subClient.subclient.edit_chat(chatId=chat, viewOnly=False)
        except:
            pass


@client.command("comment")
def comment_profile(data):
    datamess = data.message
    if datamess:
        data.subClient.comment(message=data.message, userId=data.authorId)
        data.subClient.send_message(
            chatId=data.chatId,
            message=f"{data.author} Observame comentar hasta allá")
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message=
            "Este comando es para que comente el muro con lo que tu quieras! Pon algo y yo lo comentare en tu perfil"
        )


@client.command("stickerimg")
def stickerimg(data):
    info = data.subClient.get_message_info(chatId=data.chatId,
                                           messageId=data.messageId)
    reply_message = info.json['extensions']
    if reply_message:
        image = info.json['extensions']['replyMessage']['extensions'][
            'sticker']['icon']
        filename = image.split("/")[-1]
        filetype = image.split(".")[-1]
        if filetype != "gif":
            filetype = "image"
            urllib.request.urlretrieve(image, filename)
            with open(filename, 'rb') as fp:
                data.subClient.send_message(data.chatId,
                                            file=fp,
                                            fileType=filetype)
                os.remove(filename)


@client.command("stickergif")
def stickergif(data):
    info = data.subClient.get_message_info(chatId=data.chatId,
                                           messageId=data.messageId)
    reply_message = info.json['extensions']
    if reply_message:
        image = info.json['extensions']['replyMessage']['extensions'][
            'sticker']['icon']
        filename = image.split("/")[-1]
        filetype = image.split(".")[-1]
        if filetype != "image":
            filetype = "gif"
            urllib.request.urlretrieve(image, filename)
            with open(filename, 'rb') as fp:
                data.subClient.send_message(data.chatId,
                                            file=fp,
                                            fileType=filetype)
                os.remove(filename)


@client.command("ban", is_it_me)
def ban(data):
    mention = data.subClient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        data.subClient.subclient.ban(userId=str(user),
                                     reason=f"{data.author}:Ban ban ban")
        data.subClient.send_message(
            data.chatId,
            message=
            "Como quitarle el dulce a un niño, comerselo y reirse mientras llora"
        )


@client.command("shu", is_it_me)
def banchat(data):
    mention = data.subClient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        data.subClient.subclient.kick(userId=str(user),
                                      chatId=data.chatId,
                                      allowRejoin=True)
        data.subClient.send_message(data.chatId,
                                    message="no vuelvas")


@client.command("banchat", is_it_me)
def banchat(data):
    mention = data.subClient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        data.subClient.subclient.kick(userId=str(user),
                                      chatId=data.chatId,
                                      allowRejoin=False)
        data.subClient.send_message(data.chatId,
                                    message="Te pasa, por imbecil")


@client.command("warn", is_it_me)
def warn(data):
    mention = data.subClient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        data.subClient.subclient.warn(
            userId=str(user),
            reason=f"{data.author}advertencia advertencia advertencia")
        data.subClient.send_message(
            data.chatId, message="Te lo aviso, una más y no será agradable")


@client.command("strike", is_it_me)
def strike(data):
    mention = data.subClient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        data.subClient.subclient.strike(
            userId=str(user),
            time="1",
            title="strike a strike",
            reason=f"{data.author} strike strike strike")
        data.subClient.send_message(data.chatId,
                                    message="Una falta, de mi parte para ti")


@client.command("hostt")
def hostt(data):
    mention = data.subClient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        data.subClient.subclient.transfer_host(
            chatId=data.chatId,
            userIds=str(user),
        )
        data.subClient.send_message(data.chatId, message="Host")


@client.command("textoabinario")
def textoabinarioo(data):
    params = data.message
    link = f'https://some-random-api.ml/binary?text={params}'
    response = requests.get(link)
    json_data = json.loads(response.text)
    textbin = json_data['text']
    if params:
        data.subClient.send_message(chatId=data.chatId,
                                    message=textbin,
                                    replyTo=data.messageId)
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message="Debes poner algo para convertir tu texto en binario!")


@client.command("unban", is_it_me)
def unban(data):
    id = client.get_from_code(data.message).objectId
    data.subClient.subclient.unban(userId=id,
                                   reason=f"{data.author}:unban unban unban")
    data.subClient.send_message(data.chatId, message="Bien, ya puede regresar")


@client.command("fonttxt")
def fancytext(data):
    msg = data.message + " null "
    msg = msg.split(" ")
    msg[1] = msg[0]
    data.subClient.send_message(data.chatId, message=fancy.light(msg[1]))
    data.subClient.send_message(data.chatId, message=fancy.bold(msg[1]))
    data.subClient.send_message(data.chatId, message=fancy.box(msg[1]))
    data.subClient.send_message(data.chatId, message=fancy.sorcerer(msg[1]))


@client.command("icon", is_it_me)
def icon(data):
    info = data.subClient.subclient.get_message_info(chatId=data.chatId,
                                                     messageId=data.messageId)
    reply_message = info.json['extensions']
    if reply_message:
        image = info.json['extensions']['replyMessage']['mediaValue']
        for i in range(1, 5):
            data.subClient.subclient.edit_profile(icon=image)
    data.subClient.send_message(
        data.chatId,
        message="Mi icon ha sido cambiado por el que me han enviado",
        replyTo=data.messageId)


@client.command("bgperfil", is_it_me)
def fondoperfil(data):
    info = data.subClient.subclient.get_message_info(chatId=data.chatId,
                                                     messageId=data.messageId)
    reply_message = info.json['extensions']
    if reply_message:
        image = info.json['extensions']['replyMessage']['mediaValue']
        for i in range(1, 5):
            data.subClient.subclient.edit_profile(backgroundImage=image)
    data.subClient.send_message(
        data.chatId,
        message="Mi fondo de perfil ha sido cambiado por el que me han enviado",
        replyTo=data.messageId)


@client.command("globallink")
def get_global(data):
    objectId = client.get_from_code(data.message).objectId
    data.subClient.send_message(data.chatId,
                                message="ndc://g/user-profile/" + objectId,
                                replyTo=data.messageId)


@client.command("shipp")
def ship(data):
    ship = random.choice([
        "Tienen un 50% parecen ser buenos amigos, lo mejor es que sean amigos.. >w<",
        "Tienen un 90% son compatibles entre ellos dos, podrìan   ser pareja.. >w<",
        "Tienen un 99% son compatibles entre ellos dos, porfavor contraigan matrimonio malditos.>w<",
        "Tienen un 49% son conocidos y realmente puede que tengan una simple amistad. :/",
        "Tienen un 20% son como el agua y el aceite, no pueden combinarse y es mejor no ser ni conocidos. >w<",
        "Tienen un 1% son como el agua y el aceite, no pueden combinarse y es mejor no ser ni conocidos. >w<"
    ])
    data.subClient.send_message(
        data.chatId,
        message=f"{data.author} y {data.message} {ship}",
        replyTo=data.messageId)

@client.command("global")
def globall(data):
    mention = data.subClient.subclient.get_message_info(
        chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        AID = client.get_user_info(userId=str(user)).aminoId
        data.subClient.send_message(data.chatId,
                                    message="https://aminoapps.com/u/" +
                                    str(AID))


@client.command("encontrar")
def get_people(data):
    objectId = client.get_from_code(data.message).objectId
    data.subClient.send_message(data.chatId,
                                message="ndc://user-profile/" + objectId)


@client.command("sigueme")
def seguir(data):
    data.subClient.send_message(
        data.chatId,
        f'Haré todo lo que me pidas {data.author} promesita del meñique')
    data.subClient.follow_user(data.authorId)


@client.command("duckgo")
def duckgo(data):
    datamess = data.message
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    if datamess:
        data.subClient.send_message(
            chatId=data.chatId,
            message=f"https://duckduckgo.com/?q={msg}&t=h_",
            replyTo=data.messageId)
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message=
            "Este comando es para hacer una busqueda! Pon lo que quieras buscar y lo enviare por ti."
        )


@client.command("chiste")
def chistes(data):
    chistess = c.get_random_chiste()
    data.subClient.send_message(data.chatId, chistess, replyTo=data.messageId)


@client.command("twitter")
def twitter(data):
    datamess = data.message
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    if datamess:
        data.subClient.send_message(
            chatId=data.chatId,
            message=f"https://twitter.com/search?q={msg}&src=typed_query",
            replyTo=data.messageId)
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message=
            "Este comando es para hacer una busqueda en Twitter! Pon lo que quieras buscar y lo enviare por ti."
        )


@client.command("yahoo")
def yahoo(data):
    datamess = data.message
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    if datamess:
        data.subClient.send_message(
            chatId=data.chatId,
            message=f"https://search.yahoo.com/search?p={msg}",
            replyTo=data.messageId)
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message=
            "Este comando es para hacer una busqueda! Pon lo que quieras buscar y lo enviare por ti."
        )


@client.command("unfollow")
def unfollow(data):
    data.subClient.unfollow_user(data.authorId)
    data.subClient.send_message(data.chatId,
                                f"Te he dejado de seguir {data.author}.. :c")


@client.command("fondo")
def bg(data):
    image = data.subClient.get_chat_thread(chatId=data.chatId).backgroundImage
    if image:
        filename = path.basename(image)
        urllib.request.urlretrieve(image, filename)
        with open(filename, 'rb') as fp:
            data.subClient.send_message(data.chatId, file=fp, fileType="image")
        os.remove(filename)
        data.subClient.send_message(
            data.chatId,
            message=f"{data.author} aquí tienes el fondo del chat",
            replyTo=data.messageId)
    else:
        data.subClient.send_message(data.chatId,
                                    message="No hay fondo en este chat!")


@client.command("unete", is_it_me)
def joinvc(data):
    client.join_screen_room()
    data.subClient.send_message(
        data.chatId,
        message=f"{data.author} es bueno ser necesitado",
        replyTo=data.messageId)


@client.command("pedido")
def pedido(data):
    data.subClient.send_message(
        data.chatId,
        message=
        """¿Quieres un bot igual a este o personalizado por ti? Contacta con mi Creadora
      
      http://aminoapps.com/u/Shelpek""",
        replyTo=data.messageId)


@client.answer("admin", is_it_me)
def migranadmin(data):
    data.subClient.send_message(data.chatId,
                                message=f"""{data.author} es mi admin""",
                                replyTo=data.messageId)


@client.answer("Elena")
def hello(data):
    dreven = random.choice([
        "¿Y ahora que quieres?", "¿Me extrañaste? Yo a ti no",
        "¿Necesitas mi ayuda? ¿Por qué no me sorprende?",
        "¿Necesitas ayuda, cierto? Utiliza !help y entraras en un mundo magico",
        "Y la chingada como molestas"
    ])
    data.subClient.send_message(data.chatId, dreven, replyTo=data.messageId)

@client.answer("Elena chilena")
def hello(data):
    dreven = random.choice([
        "La wea random po weon qliao", "Ya po weon yo no hablo raro weon wa weona na weona qlia de la weon wea", "Ya cachai que no se de la wea del weon que weaba el puro weonazo", "se que hay weones que weonean la pura wea", "chile no habla raro, Chile: ya cachai que cacho cachò la pura wea del cachon?", "Yo sabia que habian weones que weonaban el puro pico del weon", "Si cachai la wea weona weon dejate de andar webiandome con la wea"
    ])
    data.subClient.send_message(data.chatId, dreven, replyTo=data.messageId)  

@client.answer("sexo")
def hello(data):
    dreven = random.choice([
        "SEXOOOOOOOOO", "Callate y cogeme", "Acto de la reproduccion humana", "no juan ya te dije que no te voy a dar mis patas para que te masturbes con ellas", "osi sexo sexo", "dame como cajon que no cierra", "siempre quise que llegara este momento, S E X O"
    ])
    data.subClient.send_message(data.chatId, dreven, replyTo=data.messageId)  

@client.answer("monedero")
def hello(data):
    dreven = random.choice([
        "[Aqui puedes donarme = http://aminoapps.com/p/dsrcome]"
    ])
    data.subClient.send_message(data.chatId, dreven, replyTo=data.messageId)  

@client.answer("Hola")
def hello(data):
    dreven = random.choice([
        "Hola esto hola aquello, cogemos?", "Hola, soy Elena, chupame los pies",
        "Hola, puta/o",
        "Hola mi amor", "Hola hola, aqui llego la mas perrona",
        "Y la chingada como molestas, me vale mierda tu hola", "CALLATE"
    ])
    data.subClient.send_message(data.chatId, dreven, replyTo=data.messageId)  


@client.answer("Elena dime tu anime favorito")
def hello(data):
    dreven = random.choice(["¿Anime? No digas idioteces y juega Call Of Duty"])
    data.subClient.send_message(data.chatId, dreven, replyTo=data.messageId)

@client.answer("Elena puta")
def hello(data):
    dreven = random.choice(["Puta tu mama", "Si pero bien que usas mis comandos", "Mentira el unico puto aqui eres tu", "Asi es, vamos a la cama", "Como lo ordenaste, yo soy la puta y tu la zorra malparida", "Callate y besame los pies como la basura que eres"])
    data.subClient.send_message(data.chatId, dreven, replyTo=data.messageId)  

@client.answer("Elena inutil")
def hello(data):
    dreven = random.choice(["Anda por gracioso/a ya no tienes acceso a mis comandos"])
    data.subClient.send_message(data.chatId, dreven, replyTo=data.messageId)

@client.answer("Estupido bot")
def hello(data):
    dreven = random.choice(["Estupido? Tengo la capacidad de expulsarte del chat, dime estupida denuevo, anda."])
    data.subClient.send_message(data.chatId, dreven, replyTo=data.messageId)

@client.answer("te amo")
def drevlover(data):
    drevlove = random.choice([
        "¡Ja! yo no puedo amarte, animal.",
        "Y yo a ti. Mira, aprendí a mentir", "Claro, ya lo sé ¿Quién np?", "yo te amo mas",
      "Pero.. lo nuestro no es posible", "Te adoro me encantas y te amo", "mi amor prohibido", 
      "rawr te amu"
    ])
    data.subClient.send_message(data.chatId, drevlove, replyTo=data.messageId)


@client.answer("windows")
def windowsdrev(data):
    windrev = random.choice(["¡Tontito! Como vas a usar esa cosa, usa Linux"])
    data.subClient.send_message(data.chatId, windrev, replyTo=data.messageId)


#@client.command("habla")
#def habla(data):
#    data.subClient.send_message(data.chatId, message=f"{data.author} {data.message}", replyTo = data.messageId)


@client.command("habla")
def say_something(data):
    audio_file = f"sound/ttp.mp3"
    gTTS(text=data.message, lang='es', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)
   


@client.command("help")
def helpdrev(data):
    data.subClient.send_message(chatId=data.chatId,
                                message="""[BC]Y aquí vamos otra vez❢
[c]ꔛ  𑁍︎  ꔛ  𑁍︎  ꔛ  𑁍︎  ꔛ
[C]Hola,  ¿qué tal? Mi nombre
[C]es ╰ Elena ╯  y estoy  aqui para
[C]ayudarte   para    eso   me,  programaron te diré mis comandos
[C]cuales están separados en
[C]las  siguientes  categorías:
[C]︿︿︿︿︿︿︿︿︿𖡼.𖤣𖥧.𖧧
[C]. 𐑺 !cutes           . 𐑺 !entretenimiento
[C]. 𐑺 !acciones     . 𐑺 !dueño
[C]. 𐑺 !chats
[c]
[C][ 評議会 ]        ¡!       
[Cu]𖧧 Para ver  los  comandos
[Cu]𖧧 pon el nombre de cada
[Cu]𖧧 categoría  en   el  chat.

[C]Ejemplo: !cutes
[C]꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷""",
                                replyTo=data.messageId)


@client.command()
def cutes(data):
    data.subClient.send_message(data.chatId,
                                message="""[bc]⤥〃𝐂ut᷍es༴ 

[c]casarse • divorcio  • monedero • shipp • abrazar • besar • mejilla • sonrojarse • morder • cosquillas • pat • guiño • timido • alimentar • enamorado • sonreir • llora • shippname •"""
                                )


@client.command()
def chats(data):
    data.subClient.send_message(data.chatId,
                                message="""[bc]⤥〃𝐂hat᷍s༴

[c]empezarlive • terminarlive • datos • elena chilena • sexo • te amo • Estupido bot • Elena inutil • Elena puta • Windows • "Elena dime tu anime favorito" • "Elena" • pedido • unete • coin • checkin • all • terminosuser • test • activos • pvp"""
                                )


@client.command()
def acciones(data):
    data.subClient.send_message(data.chatId,
                                message="""[bc]⤥〃𝐀ccio᷍nes༴

[c]hifives • pegar • patada • gay • sex • luffy • enojao • comer • carcel • teta • saltar • muslos • correr • huir • enojado • beber • jugar •dibujar • bailar • suicidio • libreta • selfie • nalguear"""
                                )


@client.command()
def entretenimiento(data):
    data.subClient.send_message(data.chatId,
                                message="""[bc]⤥〃𝐄ntreten᷍imiento༴

[c] •!wiki • habla • img • google • • meow • duckgo • tra • askme • reto • stickerimg • stickergif • chiste • fondo • fonttxt • neontxt • version • simp • loli • pixel • horny • menciona • id • disclaimer • comment • global • globallink • sigueme • twitter • sigueme • unfollow • yahoo • tra • tra-en • chat • voz • voz-pt • voz-ja • idlink • version • letra • perro • gato • zorro • koala • jahy • wallpaperpc • wallpapermovil • snowtxt • gradienttxt • summtxt • rgbtxt"""
                                )


@client.command()
def dueño(data):
    data.subClient.send_message(data.chatId,
                                message="""[bc]⤥〃𝐃ue᷍ño༴
[C]• banchat •[!kickchat] y Pones El usuario con el aroba para expulsarlo • name • bgperfil • icon • joinchat • leavechat • coanfi • bloquear • desbloquear • bienvenidamuro • reiniciar • bio • view • unview • descripcion • titlechat • titulo • quitar • aminojoin • apagar • unwelcome"""
                                )


@client.command("correr")
def corriendogif(data):
    corriendogifs = random.choice([
        "https://i.pinimg.com/originals/0e/1f/60/0e1f6056879553d529bf5a9dd4711f01.gif",
        "https://pa1.narvii.com/6811/479c08484c30795e57054a68389e17cb3381b63b_hq.gif",
        "https://c.tenor.com/A9UoQ6-_2YQAAAAC/nezuko-running.gif"
    ])
    url = corriendogifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"esta haciendo ejercicio corriendo como naruto.. >w<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("google")
def google(data):
    datamess = data.message
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    if datamess:
        data.subClient.send_message(
            chatId=data.chatId,
            message=f"https://www.google.com/search?q={msg}",
            replyTo=data.messageId)
    else:
        data.subClient.send_message(
            chatId=data.chatId,
            message=
            "Este comando es para hacer una busqueda! Pon lo que quieras buscar y lo enviare por ti."
        )



# !wiki
@client.command("wiki")
def wiki(data):
    # Tome la página y el resumen y luego divídalo para que pueda caber en el límite
    try:
        wp = wikipedia.page(data.message)
    except wikipedia.exceptions.DisambiguationError as e:
        # Si aterriza en una página de desambiguación, imprime un error
        may_referir_a = '\n[c]'.join(e.options)
        data.subClient.send_message(
            data.chatId,
            esteticabase("Desambiguación", f"""[c]{may_referir_a}""",
                         f"{data.message} Puede referirse a: "))
        return False
    wpr = wp.content.split("\n")

    # Manda o primeiro paragrafo
    data.subClient.send_message(
        data.chatId,
        esteticabase(wp.title, f"""[c]{wpr[0]}

#[c]Mas información en: {wp.url}""", f"Resumen de {wp.title}"))


@client.command("tra")
def tra(data):
    translator = google_translator()
    translate_textes = translator.translate(data.message, lang_tgt='es')
    data.subClient.send_message(data.chatId,
                                f"{translate_textes}",
                                replyTo=data.messageId)


@client.command("tra-en")
def tra(data):
    translator = google_translator()
    translate_text = translator.translate(data.message, lang_tgt='en')
    data.subClient.send_message(data.chatId,
                                f"{translate_text}",
                                replyTo=data.messageId)


@client.command("askme")
def ball(data):
    ball = random.choice([
        "No.", "Sì.", "Tal vez.", "Claro.", "Nunca.", "Claro que sì.",
        "Porque si.", "Eres pelotudo.", "Tu mama",
        "Claro que no, no haria eso.",
        "No estoy interesado en responderte, niño@",
        "Tu inteligencia no llega a mucho."
    ])
    data.subClient.send_message(data.chatId, ball, replyTo=data.messageId)


@client.command("meow")
def ball(data):
    ball = random.choice([
        "Meow Daddy~.", "Meow.", "Solo porque me lo pides tu.. Meow~.",
        "Meow Mommy~",
        "P-pero.. bueno lo hare pero porque quiero. M-meow U-uhg~",
        "M-mommy.. alimentame, meow~", "Miau gatita feliz"
    ])
    data.subClient.send_message(data.chatId, ball, replyTo=data.messageId)


@client.command("reto")
def reto(data):
    reto = random.choice([
        "Besar a alguien del grupo.", "Cantar y bailar como loco/a.",
        "Declararte a la persona que te gusta.",
        "Llama a algún número desconocido y canta feliz cumpleaños.",
        "Deberás hablar cantando durante cinco minutos",
        "Escribe un poema con las 5 palabras elegidas por los otros jugadores",
        "Imita una emisión de televenta durante 3 minutos",
        "Cuentame un secreto.",
        "Envia las ultimas 5 fotos de tu galeria.. >.<", "Ser mi novio/a :3"
    ])
    data.subClient.send_message(data.chatId, reto, replyTo=data.messageId)


"""""
bienvenida
""" ""
"""
def goodChat(data):
  return data.chatId in ("fb6d06aa-a483-4bf1-a873-e3dd8593498b")
"""


@client.command("voz")
def say_something(data):
    audio_file = f"{path_download}/ttp.mp3"
    gTTS(text=data.message, lang='en', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)

@client.command("voz-pt")
def say_something(data):
    audio_file = f"{path_download}/ttp.mp3"
    gTTS(text=data.message, lang='pt', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)  

@client.command("voz-ja")
def say_something(data):
    audio_file = f"{path_download}/ttp.mp3"
    gTTS(text=data.message, lang='ja', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)      


@client.command("titulo", is_it_me)
def title(data):
    if client.check(data, 'staff', id_=client.botId):
        try:
            title, color = data.message.split("color=")
            color = color if color.startswith("#") else f'#{color}'
        except Exception:
            title = data.message
            color = None

        if data.subClient.add_title(data.authorId, title, color):
            data.subClient.send_message(
                data.chatId, f"Listo, ya tienes tu titulo, no abuses.. >w<")


@client.command("quitar", is_it_me)
def remove_titulo(data):
    data.subClient.remove_title(data.authorId, data.message)
    data.subClient.send_message(chatId=data.chatId,
                                message="Listo, ya he quitado tu titulo.")


@client.on_member_leave_chat()
def say_goodbye(data):
    imagen = rutas("good bye")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(
            data.chatId,
            embedContent=f"¡En lugar de venirse se fue! Que imbecil",
            file=aud,
            fileType="gif")


@client.event("on_voice_message")
def on_audio(data):
    print("Audio Enviado")


@client.event("on_chat_tip")
def on_chat_tip(data):
    try:
        commuId = data.json["ndcId"]
        subClient = communaute[commuId]
    except Exception:
        return
    raw_data = data.json
    nick_name = raw_data['chatMessage']['author']['nickname']
    coins = raw_data['chatMessage']['extensions']['tippingCoins']
    chatId = raw_data['chatMessage']['threadId']
    reply = "[C]¡Gracias por tus " + str(coins) + " Coins! \n\n[C]" + str(
        nick_name)
    print(raw_data)
    print("chatId", chatId)
    data.subClient.send_message(chatId=chatId, message=reply)


#Acciones.


@client.command("gif")
def gif(data):
    search = (data.message)
    with suppress(Exception):
        try:
            data.subClient.delete_message(data.chatId,
                                          data.messageId,
                                          asStaff=True)
        except:
            data.subClient.delete_message(data.chatId, data.messageId)
    response = requests.get('http://api.giphy.com/v1/gifs/search?q=' + search +
                            '&api_key=S13D1syQMbuM7kGC3Kw721Z2OwOYyQeG')
    # print(response.text)
    data = json.loads(response.text)
    gif_choice = randint(0, 9)
    image = data['data'][gif_choice]['images']['original']['url']
    print("URL", image)
    if image is not None:
        print(image)
        filename = image.split("/")[-1]
        urllib.request.urlretrieve(image, filename)
        with open(filename, 'rb') as fp:
            data.subClient.send_message(data.chatId, file=fp, fileType="gif")
            print(os.remove(filename))


@client.command("hifives")
def hifivegif(data):
    hifivegifs = random.choice([
        "https://c.tenor.com/_KGWqG2EBdIAAAAC/anime-girls.gif",
        "https://c.tenor.com/ctl_4NqVGkMAAAAd/meliodas-friends.gif",
        "https://c.tenor.com/i3wzYOB5XysAAAAC/yes-high-five.gif",
        "http://4.bp.blogspot.com/-zFgKJCMQY0s/VCh7Q7B6NCI/AAAAAAAAUbQ/RQu02-605Uw/s1600/Futs%C5%AB%2Bno%2BJoshik%C5%8Dsei%2Bga%2BLocodol%2BYattemita2.gif"
    ])
    url = hifivegifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"ha chocado los cincos con {data.message}.. >w<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("llora")
def lloragif(data):
    lloragifs = random.choice([
        "https://c.tenor.com/EFBwy6rvcXEAAAAC/sad-anime.gif",
        "https://mkgifs.com/wp-content/uploads/2022/03/Tanjiro-sad-gif.gif",
        "https://c.tenor.com/gqkjE1ZY3_MAAAAd/jahy-jahy-sama.gif"
    ])
    url = lloragifs
    file = url_like(url)

    data.subClient.send_message(data.chatId,
                                embedContent=f"esta llorando.. :((",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="gif")


@client.command("besar")
def besargif(data):
    besargifs = random.choice([
        "https://c.tenor.com/tNClex-tMZQAAAAC/kiss-beso.gif",
        "https://i.pinimg.com/originals/49/7a/55/497a5523d9b1ca23db84ecc3f5d8b1b3.gif",
        "https://i.gifer.com/2Lmc.gif",
        "https://64.media.tumblr.com/ba1d2520a76b9c0dd40b971d7a987a52/tumblr_nbl7d3jLuD1tz85kto1_500.gif",
        "https://c.tenor.com/Yu-sfUdLMAUAAAAC/koi-to-uso-anime.gif",
        "https://pa1.narvii.com/6048/2fabab7e31ef8d545acef4373a3807e220fd971c_hq.gif",
        "https://pa1.narvii.com/6430/304d4ed829d894a70d1db64568302059f8446e7f_hq.gif",
        "https://c.tenor.com/SZUxOrwuypgAAAAd/beso-kiss.gif",
        "https://c.tenor.com/cLoax6i1w34AAAAC/citrus-anime-kiss.gif",
        "https://pa1.narvii.com/6185/20223264e0180f72bebf50adba0a949e14b7e510_hq.gif"
    ])
    url = besargifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"ha besado apasionadamente a {data.message}.. :33",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("mejilla")
def mejillagif(data):
    mejillagifs = random.choice([
        "https://i.pinimg.com/originals/97/2c/2e/972c2eb564b9936ab05ffa960c1c632e.gif",
        "https://acegif.com/wp-content/uploads/anime-kiss-19.gif",
        "https://c.tenor.com/HrxtQWBHI6cAAAAC/diane-kiss.gif",
        "http://pa1.narvii.com/6120/d684eb880876c41a223386f8ba34179689b220c7_00.gif",
        "https://c.tenor.com/Yu2a1FmxFK8AAAAC/love-sweet.gif",
        "https://c.tenor.com/wr6fXkybDbkAAAAC/girl-anime.gif",
        "https://c.tenor.com/JQ9jjb_JTqEAAAAC/anime-kiss.gif",
        "https://c.tenor.com/EQeihkM16pUAAAAC/anime-kiss.gif",
        "http://i.skyrock.net/5079/88775079/pics/3174561165_1_11_1IKppSSS.gif",
        "https://img1.ak.crunchyroll.com/i/spire2/39fbc1e8ba8e7431d79494e53bee6de31536441455_full.gif"
    ])
    url = mejillagifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"ha besado en la mejilla a {data.message}.. :33",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("cosquillas")
def cosquillasgif(data):
    cosquillasgifs = random.choice([
        "https://c.tenor.com/PXL1ONAO9CEAAAAM/tickle-laugh.gif",
        "https://c.tenor.com/L5-ABrIwrksAAAAC/tickle-anime.gif",
        "https://c.tenor.com/ymMtVnW-TrYAAAAd/nekopara-anime.gif",
        "https://pa1.narvii.com/6350/885268cd63e16e4404a071f6423f1f80728c367c_hq.gif"
    ])
    url = cosquillasgifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"le esta haciendo cosquillas a {data.message}.. >w<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("abrazar")
def abrazargif(data):
    response = requests.get('https://some-random-api.ml/animu/hug')
    json_data = json.loads(response.text)
    url = json_data['link']
    file = url_like(url)

    data.subClient.send_message(
        chatId=data.chatId,
        embedContent=f"ha apapuchado a {data.message}.. :33",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.answer("dale un abrazo")
def abrazargiff(data):
    response = requests.get('https://some-random-api.ml/animu/hug')
    json_data = json.loads(response.text)
    url = json_data['link']
    file = url_like(url)

    data.subClient.send_message(
        chatId=data.chatId,
        embedContent=f"Le he apapuchado a esa hermosa persona.. ₍ᐢ. .ᐢ",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.answer("dale un pat")
def patpatpat(data):
    response = requests.get('https://some-random-api.ml/animu/pat')
    json_data = json.loads(response.text)
    url = json_data['link']
    file = url_like(url)

    data.subClient.send_message(
        chatId=data.chatId,
        embedContent=f"Le he dado un pat a esa hermosa persona.. ₍ᐢ. .ᐢ₎",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("pegar")
def golpesgif(data):
    hitgifs = random.choice([
        "https://c.tenor.com/XhdHGRof6WEAAAAM/anime-ataque-golpe-en-la-pared.gif",
        "https://i.gifer.com/I5LT.gif",
        "https://c.tenor.com/FaXcxpmU3PMAAAAC/anime-slap.gif",
        "https://c.tenor.com/Qpe8tbJURvgAAAAC/eromanga-slap.gif",
        "https://c.tenor.com/mKX_7m0GsVAAAAAC/anime-blends.gif",
        "https://c.tenor.com/xc19_U9dSNMAAAAC/chika-fujiwara-hit.gif"
    ])
    url = hitgifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"ha golpeado fuertemente a {data.message}.. >.<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("morder")
def mordergif(data):
    mordidasgifs = random.choice([
        "https://pa1.narvii.com/6547/3b0256b46869d86c221a3df4a161bf874d3ab017_hq.gif",
        "http://pa1.narvii.com/6354/9cb8a8d8aa07f7f2f4ae47a6b194fb1cb9a1afb3_00.gif",
        "https://c.tenor.com/noV5mMA7T8oAAAAM/loli-bite.gif",
        "https://pa1.narvii.com/6228/66a5591c766f364b62da5d77370861c796faa390_hq.gif"
    ])
    url = mordidasgifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"ha mordido a {data.message}.. >//<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("patada")
def patadagif(data):
    patadagifs = random.choice([
        "https://i.pinimg.com/originals/b1/94/a9/b194a9ce557297165aafc3046a671744.gif",
        "https://pa1.narvii.com/6357/385a2be62f29d48c5bb17b1394d167f06da83ba5_hq.gif",
        "https://i.gifer.com/8DpL.gif",
        "https://c.tenor.com/dOkrN01Cc0wAAAAC/dodginaaa-anime.gif"
    ])
    url = patadagifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"le ha dado una patada K.O a {data.message}.. >.<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("sonrojarse")
def sonrojarsegif(data):
    sonrojadogifs = random.choice([
        "https://c.tenor.com/jV9COSlMsBkAAAAd/sonrojo-cyan.gif",
        "https://pa1.narvii.com/6103/ea55b9171ee7210eafcb4e2ed554d77dd4dfcc2d_hq.gif",
        "https://i.pinimg.com/originals/ef/d5/38/efd53867ad9691d7cace6a30c5d7d865.gif",
        "https://animesher.com/orig/1/136/1366/13666/animesher.com_sonrojo-orejitas-acchi-kocchi-1366659.gif"
    ])
    url = sonrojadogifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"ha sido sonrojado por {data.author}.. >//<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("img")
def imagenes(data):
    randomimg = random.choice([
        "https://www.anmosugoi.com/wp-content/uploads/2021/08/Jahy-Sama-wa-Kujikenai-11.jpg",
        "https://i.pinimg.com/736x/3c/9c/d4/3c9cd4ed30e5fac7b3ece7ccbca84fa9.jpg"
    ])
    url = randomimg
    file = url_like(url)

    data.subClient.send_message(data.chatId, file=file, fileType="image")


@client.command("audio")
def audios(data):
    randomaudio = random.choice([
        "https://drevenzz.com/audio/random/1.mp3",
        "https://drevenzz.com/audio/random/2.mp3",
        "https://drevenzz.com/audio/random/3.mp3",
        "https://drevenzz.com/audio/random/4.mp3",
        "https://drevenzz.com/audio/random/5.mp3",
        "https://drevenzz.com/audio/random/6.mp3",
        "https://drevenzz.com/audio/random/7.mp3",
        "https://drevenzz.com/audio/random/8.mp3",
        "https://drevenzz.com/audio/random/9.mp3",
        "https://drevenzz.com/audio/random/10.mp3",
        "https://drevenzz.com/audio/random/11.mp3",
        "https://drevenzz.com/audio/random/12.mp3",
        "https://drevenzz.com/audio/random/13.mp3",
        "https://drevenzz.com/audio/random/14.mp3",
        "https://drevenzz.com/audio/random/15.mp3",
        "https://drevenzz.com/audio/random/16.mp3"
    ])
    url = randomaudio
    file = url_like(url)

    data.subClient.send_message(data.chatId, file=file, fileType="audio")


@client.command("baki")
def audios(data):
    audios = rutas("baki audios")
    with open(str(random.choice(audios)), "rb") as aud:
        data.subClient.send_message(
            data.chatId,
            file=aud,
            fileType="audio")      

@client.command("casarse")
def casarse(data):
    casarsegifs = random.choice([
        "https://i.pinimg.com/originals/02/7c/d9/027cd997f81e9410a7360085a584cdd6.gif",
        "https://acegif.com/wp-content/uploads/anime-love-53.gif"
    ])
    url = casarsegifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=
        f"Yo los declaro, marido y mujer {data.author} y {data.message} puede besar al novio/a.",
        embedTitle=f"Casamiento de {data.author} y {data.message}",
        file=file,
        fileType="gif")


@client.command("divorcio")
def divorcio(data):
    data.subClient.send_message(
        data.chatId,
        message=
        f"Oh no.. {data.author} ha decidido divorciarse de {data.message}, espero que se pudran en el infierno digo.. que les vaya bien en su vida de divorciados.. >w<"
    )


@client.command("matar")
def matargif(data):
    matargifs = random.choice([
        "https://64.media.tumblr.com/b73e4f79bbf11e331d74a4e1d4d18acc/tumblr_mxk3qzXabI1s1azceo1_500.gif",
        "http://pa1.narvii.com/6229/dfeee5bf8eb1c01c478efa7e2d6aa64f85cca5a9_00.gif"
    ])
    url = matargifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"ha acabado matando a {data.message}.. >.<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("comer")
def comergif(data):
    comergifs = random.choice([
        "https://i.pinimg.com/originals/4e/54/cc/4e54ccbf373f82cc20fe9fd3cf2bf036.gif",
        "https://c.tenor.com/r0TXbxJf1JsAAAAC/comer-pastel.gif"
    ])
    url = comergifs
    file = url_like(url)

    data.subClient.send_message(data.chatId,
                                embedContent=f"esta comiendo.. >.<",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="gif")


@client.command("alimentar")
def alimentargif(data):
    alimentargifs = random.choice([
        "https://pa1.narvii.com/6347/361cd75f09a10e757230152ac63aef369f489c04_hq.gif",
        "https://pa1.narvii.com/6049/7eae49d356f9d44eef3998e073cb8847f7ad802a_hq.gif",
        "https://c.tenor.com/3b7uYr2qLb8AAAAC/nyanko-days.gif"
    ])
    url = alimentargifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"esta alimentando a su pequeño bebe {data.message}.. :33",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("huir")
def huyendogif(data):
    huyendogifs = random.choice([
        "https://pa1.narvii.com/6139/84a53675e2f7664073f3750becaa26b408a5d990_hq.gif",
        "https://c.tenor.com/CRtScm9kMJUAAAAC/corran-corred.gif"
    ])
    url = huyendogifs
    file = url_like(url)

    data.subClient.send_message(data.chatId,
                                embedContent=f"esta huyendo de algo.. :((",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="gif")


@client.command("saltar")
def saltargif(data):
    saltargifs = random.choice([
        "https://i.pinimg.com/originals/65/c2/6e/65c26e590bbb1387cbd9366376f5f1f9.gif",
        "http://pa1.narvii.com/6154/156aa081932fdc274eb7398fd0000d2bad88ad5a_00.gif"
    ])
    url = saltargifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"esta saltando alegremente la cuerda.. >w<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("sonreir")
def sonreirgif(data):
    sonreirgifs = random.choice([
        "https://pa1.narvii.com/6621/4c502e8666f1b8012504952d07e28ac2332c949f_hq.gif",
        "https://i.pinimg.com/originals/ca/ea/f1/caeaf1d6541649bbb000ab4ad5096568.gif"
    ])
    url = sonreirgifs
    file = url_like(url)

    data.subClient.send_message(data.chatId,
                                embedContent=f"esta sonriendo.. c:",
                                embedTitle=f"{data.author}",
                                file=file,
                                fileType="gif")


@client.command("jugar")
def jugargif(data):
    jugargifs = random.choice([
        "https://c.tenor.com/2MmFAis2SjIAAAAC/chica-anime.gif",
        "https://pa1.narvii.com/6149/1cc2e4d802d040d62189a8d789cf6196df38a61e_hq.gif",
        "http://pa1.narvii.com/6044/3b44f8982a08761c0c3d9ce6385581afdfb925ab_00.gif"
    ])
    url = jugargifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"esta jugando su juego favorito.. >.<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("enojado")
def enojadogif(data):
    enojadogifs = random.choice(
        ["https://acegif.com/wp-content/gif/angry-46.gif"])
    url = enojadogifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=
        f"{data.author} esta enojado.. yo que tu no le molesto.. >.<",
        embedTitle=f"¡Cuidado! {data.author}",
        file=file,
        fileType="gif")


@client.command("dibujar")
def dibujargif(data):
    dibujargifs = random.choice([
        "https://i.pinimg.com/originals/92/dd/00/92dd00f34385cac3eab40added5539aa.gif",
        "https://c.tenor.com/LxaQ_irnwmkAAAAC/anime-anime-gif.gif"
    ])
    url = dibujargifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"esta dibujando una obra de arte.. :33",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("beber")
def bebergif(data):
    bebergifs = random.choice([
        "http://pa1.narvii.com/5698/844c0a31dd6353cd8495984ddede223cd0a04673_hq.gif",
        "https://c.tenor.com/1eWj5qLpLDcAAAAC/anime-milk-anime.gif"
    ])
    url = bebergifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"esta bebiendo su bebida favorita.. >.<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("bailar")
def bailargif(data):
    bailargifs = random.choice([
        "https://c.tenor.com/mKTS5nbF1zcAAAAd/cute-anime-dancing.gif",
        "https://c.tenor.com/clfAHFQlLYEAAAAC/anime-dance-deadman.gif"
    ])
    url = bailargifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"esta bailando al ritmo de la musica.. >w<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


@client.command("enamorado")
def enamoradogif(data):
    enamoradogifs = random.choice([
        "https://i.pinimg.com/originals/c8/69/7a/c8697a9a6804d0a53d8d2fb0fa31ae8f.gif",
        "https://acegif.com/wp-content/gif/heart-eyes-3.gif",
        "https://c.tenor.com/7CViaHUzg78AAAAC/muero-de-amor-chica.gif",
        "https://acegif.com/wp-content/uploads/anime-love-50.gif"
    ])
    url = enamoradogifs
    file = url_like(url)

    data.subClient.send_message(
        data.chatId,
        embedContent=f"se ha enamorado de {data.message}.. >//<",
        embedTitle=f"{data.author}",
        file=file,
        fileType="gif")


#Convertir Video a Audio


def telecharger(url):
    music = None
    if ("=" in url and "/" in url and " " not in url) or ("/" in url
                                                          and " " not in url):
        if "=" in url and "/" in url:
            music = url.rsplit("=", 1)[-1]
        elif "/" in url:
            music = url.rsplit("/")[-1]

        if music in os.listdir(path_sound):
            return music

        ydl_opts = {
            'format':
            'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'extract-audio':
            True,
            'outtmpl':
            f"{path_download}/{music}.webm",
        }

        with YoutubeDL(ydl_opts) as ydl:
            video_length = ydl.extract_info(url, download=True).get('duration')
            ydl.cache.remove()

        url = music + ".mp3"

        return url, video_length
    return False, False


def decoupe(musical, temps):
    size = 170
    with open(musical, "rb") as fichier:
        nombre_ligne = len(fichier.readlines())

    if temps < 180 or temps > 540:
        return False

    decoupage = int(size * nombre_ligne / temps)

    t = 0
    file_list = []
    for a in range(0, nombre_ligne, decoupage):
        b = a + decoupage
        if b >= nombre_ligne:
            b = nombre_ligne

        with open(musical, "rb") as fichier:
            lignes = fichier.readlines()[a:b]

        with open(musical.replace(".mp3", "PART" + str(t) + ".mp3"),
                  "wb") as mus:
            for ligne in lignes:
                mus.write(ligne)

        file_list.append(musical.replace(".mp3", "PART" + str(t) + ".mp3"))
        t += 1
    return file_list


@client.command("convert")
def convert(args):
    music, size = telecharger(args.message)
    if music:
        music = f"{path_download}/{music}"
        val = decoupe(music, size)

        if not val:
            try:
                with open(music, 'rb') as fp:
                    args.subClient.send_message(args.chatId,
                                                file=fp,
                                                fileType="audio")
            except Exception:
                args.subClient.send_message(
                    args.chatId,
                    "Ocurrio un error, puedes convertir hasta 9 min!")
            os.remove(music)
            return

        os.remove(music)
        for elem in val:
            with suppress(Exception):
                with open(elem, 'rb') as fp:
                    args.subClient.send_message(args.chatId,
                                                file=fp,
                                                fileType="audio")
            os.remove(elem)
        return
    args.subClient.send_message(args.chatId, "Error! Link no reconocido")


@client.answer("Elena ponme tu cancion favorita")
def drevmusic(args):
    linkmusic = random.choice([
        "https://www.youtube.com/watch?v=iK3W9kvsQ_o",
        "https://youtu.be/GP3zFD2_ThE"
    ])
    music, size = telecharger(linkmusic)
    if music:
        music = f"{path_download}/{music}"
        val = decoupe(music, size)

        if not val:
            try:
                with open(music, 'rb') as fp:
                    args.subclient.send_message(
                        args.chatId,
                        message="Recibido! Por favor espereme.. :33",
                        replyTo=data.messageId)
                    args.subClient.send_message(args.chatId,
                                                file=fp,
                                                fileType="audio")
            except Exception:
                args.subClient.send_message(
                    args.chatId,
                    "Ocurrio un error, puedes convertir hasta 9 min!")
            os.remove(music)
            return

        os.remove(music)
        for elem in val:
            with suppress(Exception):
                with open(elem, 'rb') as fp:
                    args.subClient.send_message(args.chatId,
                                                file=fp,
                                                fileType="audio")
            os.remove(elem)
        return
    args.subClient.send_message(args.chatId, "Error! Link no reconocido")


#Media by Anti

mediainfo = '''[bci]Detalles del Archivo Multimedia "{name}"

[cu]Creado en
[c]{creation}
[cu]Ultima Actualizacion
[c]{modification}
[cu]Creado por
[c]<$@{author}$>
'''


@client.command()
def guardar(data):
    nombreerror = "No has insertado un nombre para el guardado."
    noencontrado = "No Multimedia encontrada."
    nosoportado = "Tipo de Multimedia no soportada."
    if not data.message:
        return data.subClient.send_message(data.chatId, message=nombreerror)
    if not data.reply:
        return data.subClient.send_message(data.chatId, message=noencontrado)
    nombremedia = data.message
    creacion = asctime()
    known = 're'
    if data.chatId not in files:
        files[data.chatId] = {}
    if nombremedia not in files[data.chatId]:
        known = ''
        files[data.chatId][nombremedia] = {'creacion': creacion}
    tipodemedia = data.replySrc.split('.')[-1]
    if tipodemedia == 'jpg':
        tipomedia = 'imagen'
    elif tipodemedia == 'gif':
        tipomedia = 'gif'
    elif tipodemedia == 'aac':
        tipomedia = 'audio'
    else:
        return data.subClient.send_message(data.chatId, message=nosoportado)
    files[data.chatId][nombremedia].update({
        'name': nombremedia,
        'output': data.replySrc,
        'type': tipomedia,
        'author': data.author,
        'authorId': data.authorId,
        'modification': creacion
    })
    with open('mediaguardada.json', 'w+') as f:
        json.dump(files, f, indent=2)
    hechosave = f"Archivo de Multimedia creado con el nombre {nombremedia} y del tipo {tipomedia}"
    return data.subClient.send_message(data.chatId, message=hechosave)


@client.command()
def multimedia(data):
    resultado = '[bci]Multimedia Disponible\n\n'
    temp = []
    split = lambda l, sep=' ': l.split(sep)
    join = lambda l, sep=' ': sep.join(l).strip()
    for name in files.get(data.chatId, []):
        temp.append(f'— {name}')
    if temp:
        resultado += join(temp, sep='\n')
    else:
        resultado += '[ci]* No hay Multimedia Disponible *'
    return data.subClient.send_message(data.chatId, message=resultado)


@client.command()
def enviar(data):
    errornombre = 'Dame el nombre al archivo multimedia a Enviar.'
    noencontrado = '¡Multimedia no encontrada! Vea la disponible con !multimedia'
    finalizado = 'Preparare su multimedia pedida.'
    if not data.message:
        return data.subClient.send_message(data.chatId, message=errornombre)
    if data.message not in files.get(data.chatId, []):
        return data.subClient.send_message(data.chatId, message=noencontrado)
    temp = url_like(files[data.chatId][data.message]['output'])
    multitype = files[data.chatId][data.message]['type']
    return data.subClient.send_message(data.chatId,
                                       file=temp,
                                       fileType=multitype)


@client.command()
def borrar(data):
    nombreerror = 'Dame el nombre al archivo multimedia a Borrar.'
    noencontrado = '¡Multimedia no encontrada! Vea la disponible con !multimedia.'
    finalizado = f'El archivo multimedia {data.message} ha sido Borrado.'
    if not data.message:
        return data.subClient.send_message(data.chatId, message=nombreerror)
    if data.message not in files.get(data.chatId, []):
        return data.subClient.send_message(data.chatId, message=noencontrado)
    deleted = files[data.chatId].pop(data.message)
    with open('mediaguardada.json', 'w+') as f:
        json.dump(files, f, indent=2)
    return data.subClient.send_message(data.chatId, message=finalizado)


#Global


@client.command("pincomunidad")
def pincomu(data):
    client.add_linked_community(comId=data.comId)
    data.subClient.send_message(data.chatId,
                                message="Comunidad Fijada en Global!")


#Burbujas


@client.command("burbujas")
def burbujas(data):
    data.subClient.send_message(data.chatId,
                                message="""

[c]Burbujas Disponibles!

[c]1. Puddle
[c]2. Nube Rosa
[c]3. Muñeco de Nieve
[c]4. Cauldron
[c]5. Primavera
[c]6. Neon

""")


@client.command("burbuja1")
def burbujapuddle(data):
    try:
        bubble = "636d3a9c-8dfc-4f91-82fc-6219349fae55"
        data.subClient.apply_bubble(chatId=data.chatId,
                                    bubbleId=bubble,
                                    applyToAll=False)
        data.subClient.send_message(
            data.chatId,
            message="Listo! Mi burbuja ha sido cambiada en este chat!")
    except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
        data.subClient.send_message(
            data.chatId,
            message="Esta burbuja no esta entre tu Inventario de Burbujas")
        pass


@client.command("burbuja2")
def bubblehehe(data):
    try:
        bubble = "4c2d0076-8812-4023-be6a-68146bdae66d"
        data.subClient.apply_bubble(chatId=data.chatId,
                                    bubbleId=bubble,
                                    applyToAll=False)
        data.subClient.send_message(
            data.chatId,
            message="Listo! Mi burbuja ha sido cambiada en este chat!")
    except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
        data.subClient.send_message(
            data.chatId,
            message="Esta burbuja no esta entre tu Inventario de Burbujas")
        pass


@client.command("burbuja3")
def bubblehe(data):
    try:
        bubble = "5b6f3f26-498f-4776-94a7-dcae221820d6"
        data.subClient.apply_bubble(chatId=data.chatId,
                                    bubbleId=bubble,
                                    applyToAll=False)
        data.subClient.send_message(
            data.chatId,
            message="Listo! Mi burbuja ha sido cambiada en este chat!")
    except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
        data.subClient.send_message(
            data.chatId,
            message="Esta burbuja no esta entre tu Inventario de Burbujas")
        pass


@client.command("burbuja4")
def bubblehe(data):
    try:
        bubble = "ba63246f-90db-4166-b639-979fa24c7164"
        data.subClient.apply_bubble(chatId=data.chatId,
                                    bubbleId=bubble,
                                    applyToAll=False)
        data.subClient.send_message(
            data.chatId,
            message="Listo! Mi burbuja ha sido cambiada en este chat!")
    except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
        data.subClient.send_message(
            data.chatId,
            message="Esta burbuja no esta entre tu Inventario de Burbujas")
        pass


@client.command("burbuja5")
def bubblehe(data):
    try:
        bubble = "b468602e-a43e-41e3-92ec-cfcc3c5028fd"
        data.subClient.apply_bubble(chatId=data.chatId,
                                    bubbleId=bubble,
                                    applyToAll=False)
        data.subClient.send_message(
            data.chatId,
            message="Listo! Mi burbuja ha sido cambiada en este chat!")
    except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
        data.subClient.send_message(
            data.chatId,
            message="Esta burbuja no esta entre tu Inventario de Burbujas")
        pass


@client.command("burbuja6")
def bubblehe(data):
    try:
        bubble = "817c94af-9311-4856-b0a2-f02c031a09f5"
        data.subClient.apply_bubble(chatId=data.chatId,
                                    bubbleId=bubble,
                                    applyToAll=False)
        data.subClient.send_message(
            data.chatId,
            message="Listo! Mi burbuja ha sido cambiada en este chat!")
    except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
        data.subClient.send_message(
            data.chatId,
            message="Esta burbuja no esta entre tu Inventario de Burbujas")
        pass


@client.command("live")
def live(data):
    data.subClient.send_message(data.chatId,
                                message="""

[c]Comandos Disponibles!

[c]1. !empezarlive ==> Empieza El Live
[c]2. !terminarlive ==> Se sale del Live


""")


@client.command("empezarlive", is_it_me)
def startvc(data):
    client.start_vc(comId=data.comId, chatId=data.chatId)


@client.command("terminarlive", is_it_me)
def endvc(data):
    client.end_vc(comId=data.comId, chatId=data.chatId)


@client.command("videollamada")
def startVideo(data):
    client.start_video_call(comId=data.comId, chatId=data.chatId)


def rutas(ruta=getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]


@client.command("all", is_it_me)
def all(args):
    users = []
    for i in range(0, 1000, 20):
        people = args.subClient.get_chat_users(args.chatId, start=i,
                                               size=1000).userId
        for usersin in people:
            users.append(usersin)

    message = {
        'chatId': args.chatId,
        'message': f"<$Fiesta de putas$>",
        'mentionUserIds': users
    }
    args.subClient.send_message(**message)


@client.command("test")
def test(data):
    timestamp = time.time()
    data.subClient.send_message(chatId=data.chatId,
                                message=".",
                                replyTo=data.messageId)
    data.subClient.send_message(chatId=data.chatId,
                                message=f"""estado : ✓
Tiempo de procesamiento {time.time()- timestamp:.2f}s.""")


@client.on_all()
def on_message(data):
    content = str(data.message).split()
    mtype = data.info.message.type

    if (mtype == 109) | (mtype == 107) | (mtype == 110) | (mtype == 108) | (
            mtype == 111) | (mtype == 111):
        if mtype == 109 and not content:
            pass
        else:
            data.subClient.kick(chatId=data.chatId,
                                userId=data.authorId,
                                allowRejoin=True)
            data.subClient.send_message(
                data.chatId,
                f"""[C]MessageType {mtype} Te lo aviso de una vez, yo no voy a limpiar!! 
                
[C]Nombre: 
{data.author}

[C]UserId: 
{data.authorId}

[C]MessageId:
{data.messageId}.""")


@client.command("activos")
def onlinemem(data):
    o = ""
    q = data.subClient.get_online_users(start=0, size=1000)
    for uid in q.profile.nickname:
        o = o + uid + "\n"
    data.subClient.send_message(data.chatId,
                                message=f"""[c]Miembros Activos 
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
    print("done")


@client.command("nalguear")
def nalgear(data):
    imagen = rutas("nalgear")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(
            data.chatId,
            embedContent=f"ah nalgueado a {data.message}... 7u7",
            embedTitle=f"{data.author}",
            file=aud,
            fileType="gif")

@client.command("sex")
def sexo(data):
    imagen = rutas("sexo")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(
            data.chatId,
            embedContent=f"va a tener accion con {data.message}, rawr",
            embedTitle=f"{data.author}",
            file=aud,
            fileType="gif")  


@client.command("luffy")
def luffy(data):
    imagen = rutas("luffy")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(
            data.chatId,
            embedContent=f"Aqui esta nuestro rey de los piratas",
            embedTitle=f"{data.author}",
            file=aud,
            fileType="gif")   

@client.command("hack")
def hack(data):
	import time
	it=randint(500,2000)
	ist=randint(50,630)
	iss=randint(10,40)
	o=randint(1,9)
	v=randint(23,98)
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
		repa= data.subClient.get_user_info(userId=str(user)).reputation
		h=data.subClient.get_user_info(userId=str(user)).nickname
		lvl = data.subClient.get_user_info(userId=str(user)).level
		crttime = data.subClient.get_user_info(userId=str(user)).createdTime
		followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
		profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
		commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
		posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
		followed = data.subClient.get_user_info(userId=str(user)).followingCount
		#data.subClient.send_message(data.chatId,message="Are you sure(Y/N)")
		#time.sleep(5)
		data.subClient.send_message(data.chatId,message=f"Se inició la carga de la cuenta {h}...")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message="Recuperación de la dirección IP del dispositivo...")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message=f"{h} ip adresse : 192.158.{o}.{v}")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message=f"""
perfil de administrador de cuenta{h}.

Pseudo: {h}
id: {str(user)}
Cuenta creada: {crttime}
Ultimo cambio: {profilchange}
reputaciones: {repa}
Nivel de cuenta: {lvl}
Número de publicaciones creadas: {posts}
Número de comentarios en el muro del perfil : {commentz}
Número de suscriptores : {followed}
Número de suscriptores : {followers}""")
		data.subClient.send_message(data.chatId,message="Carga de archivos en el sistema...")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message=f"{it} chats encontrados de cuenta {h}.")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message=f"""
Información en el sistema de {h}...

{it} archivos encontrados
{ist} imágenes encontradas
{iss} Vídeo subido""")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message="Todos los archivos subidos al servidor.")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message="Comprobando todos los archivos...")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message="Conexión al servidor Darkweb...")
		time.sleep(7)
		data.subClient.send_message(data.chatId,message="""struct group_info init_groups = { .usage = ATOMIC_INIT(2) };

struct group_info *groups_alloc(int gidsetsize){

	struct group_info *group_info;
	int nblocks;
	int i;


	nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;
	/* Asegúrese de que siempre asignemos al menos un puntero de bloque indirecto */
	nblocks = nblocks ? : 1;
	group_info = kmalloc(sizeof(*group_info) + nblocks*sizeof(gid_t *), GFP_USER);
	if (!group_info)
		return NULL;
	group_info->ngroups = gidsetsize;
	group_info->nblocks = nblocks;
	atomic_set(&group_info->usage, 1);""")
		time.sleep(5)
		data.subClient.send_message(data.chatId,message="""	if (gidsetsize <= NGROUPS_SMALL)
		group_info->blocks[0] = group_info->small_block;
	else {
		for (i = 0; i < nblocks; i++) {
			gid_t *b;
			b = (void *)__get_free_page(GFP_USER);
			if (!b)
				goto out_undo_partial_alloc;
			group_info->blocks[i] = b;
		}
	}
	return group_info;


out_undo_partial_alloc:

	while (--i >= 0) {
		free_page((unsigned long)group_info->blocks[i]);
	}
	kfree(group_info);
	return NULL;
}



EXPORT_SYMBOL(groups_alloc);
""")
		time.sleep(5)
		data.subClient.send_message(data.chatId,message="""void groups_free(struct group_info *group_info)

{

	if (group_info->blocks[0] != group_info->small_block) {
		int i;
		for (i = 0; i < group_info->nblocks|""")
		time.sleep(5)
		data.subClient.send_message(data.chatId,message="Conectado a la Dark Web.")
		time.sleep(5)
		data.subClient.send_message(data.chatId,message=f"el dispositivo de {h} fue hackeado con éxito.")
		time.sleep(5)
		data.subClient.send_message(data.chatId,message=f"Datos de la cuenta {h} están registrados en la Darkweb...")
		data.subClient.send_message(data.chatId,message=f"<$@{h}$> tu dispositivo esta hackeado.",mentionUserIds=[str(user)])

@client.command("enojao")
def enojado(data):
    imagen = rutas("enojado")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(
            data.chatId,
            embedContent=f"Esta enojado/a con {data.message}",
            embedTitle=f"{data.author}",
            file=aud,
            fileType="gif")

@client.command("comer")
def enojado(data):
    imagen = rutas("comida")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(
            data.chatId,
            embedContent=f"Esta comiendo como loca/o",
            embedTitle=f"{data.author}",
            file=aud,
            fileType="gif")       


@client.command("teta")
def teta(data):
    imagen = rutas("tetas")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(
            data.chatId,
            embedContent=f"Le ha tocado una teta a {data.message}... 7u7",
            embedTitle=f"{data.author}",
            file=aud,
            fileType="gif")

@client.command("muslos")
def muslos(data):
    imagen = rutas("muslos")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(
            data.chatId,
            embedContent=f"Ama los muslos de  {data.message} 7u7 Riko",
            embedTitle=f"{data.author}",
            file=aud,
            fileType="gif")      


@client.command("timido")
def timido(data):
    imagen = rutas("timido")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(
            data.chatId,
            embedContent=f"Esta timido por {data.message}.. cojan 7w7 >//<",
            embedTitle=f"{data.author}",
            file=aud,
            fileType="gif")


###

client.launch(True)
print("El bot ha iniciado")


#socket
def restart():
    while True:
        time.sleep(120)
        count = 0
        for i in threading.enumerate():
            if i.name == "restart_thread":
                count += 1
        if count <= 1:
            print("Restart")
            client.socket.close()
            client.socket.start()
