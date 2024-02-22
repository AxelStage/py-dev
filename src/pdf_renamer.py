#!python3
import os

WORKPATH = r"/home/xl/ebooks/_new"

symbols = [".", "_", "-"]
strings = ["LetMeRead.net__"]
# replace the publisher
publisher = [
    "OReilly ",
    "Oreilly ",
    "Apress ",
    "Packt ",
    "CRC ",
    "Routledge ",
    "MGH ",
    "Springer Scientific ",
    "MCP ",
    "Pearson ",
    "World Scientific Publishing ",
    "No Starch Press ",
    "Jossey Bass ",
    "M ",
    "Nova Science Publishers ",
    "Springer ",
    "Wiley ",
    "The MIT Press ",
    "MK ",
    "Mc Press ",
    "Microsoft Press ",
    "JB ",
    "CUP ",
    "AP ",
    "Sybex ",
    "The MIT ",
    "WSC ",
    "Academic Press ",
    "Oxford University Press ",
    "Industrial Press ",
    "Academic Press ",
    "AW ",
    "Cambridge University Press ",
    "Cengage ",
    "Manning ",
    "AMA ",
    "Sams Publishing ",
    "Prentice Hall ",
    "SPress ",
    "BCS ",
    "Cognella Academic Publishing ",
    "PacktPub ",
    "DK ",
    "Red gate books ",
    "Bloomsbury ",
    "Razeware LLC ",
    "MgH ",
    "Princeton University Press ",
    "SitePoint ",
    "Hands On ",
    "ACBooks ",
    "Publishing ",
    "LetMeRead net  ",
    "NOLO ",
    "AP Software ",
    "Pragmatic Bookshelf ",
]

input_name = os.listdir(WORKPATH)
output_name = input_name.copy()

for idx, itm in enumerate(output_name):

    # remove string at beginning
    for y, itm in enumerate(strings):
        output_name[idx] = output_name[idx].replace(itm, "")

    # add space
    for y, itm in enumerate(symbols):
        output_name[idx] = output_name[idx].replace(itm, " ")

    # remove publisher
    for y, itm in enumerate(publisher):
        output_name[idx] = output_name[idx].replace(itm, "")

    # add dot to pdf
    output_name[idx] = (
        output_name[idx].replace(" pdf", ".pdf").replace(" ebup", ".ebup")
    )

# rename
for idx, itm in enumerate(input_name):
    os.rename(
        os.path.join(WORKPATH, input_name[idx]),
        os.path.join(WORKPATH, output_name[idx]),
    )
