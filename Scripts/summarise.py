import pathlib
import os

NotesPath = pathlib.Path(__file__).parent.resolve().joinpath("../Notes").resolve()
SummaryFilePath: str

if len(list(NotesPath.glob("SUMMARY.md"))) != 1:
    print("Failed to locate a unique SUMMARY.md file!")
    quit()
else:
    SummaryFilePath = list(NotesPath.glob("SUMMARY.md"))[0]

print("Located summary file at " + str(SummaryFilePath))

NotesDirectoryList = ["Reconnaissance", "Exploitation", "Post Exploitation", "Malware Analysis", "Malware Development", "Reverse Engineering", "Hardware Hacking" , "Cryptography", "Networking"]

def SummariseDirectoryRecursively(Dir: str, OutputFile, Counter = 1):
    OutputFile.write("\t" * (Counter - 1) + "- [{}]({})\n".format(Dir[Dir.rfind("/") + 1:], NotesPath.joinpath(Dir).joinpath("index.md").relative_to(NotesPath).as_posix().replace(" ", "%20")))
    SubDirs = [f.name for f in os.scandir(NotesPath.joinpath(Dir)) if f.is_dir()]

    for SubDir in SubDirs:
        if SubDir == "Resources":
            continue
        SummariseDirectoryRecursively(Dir + "/" + SubDir.replace("\\\\", "/"), OutputFile, Counter + 1)

    Files = [f for f in NotesPath.joinpath(Dir).iterdir() if f.is_file()]
    for File in Files:
        if File.name == "README.md" or File.name == "index.md" or not File.name.endswith(".md"):
            continue
        OutputFile.write("\t" * Counter + "- [{}]({})\n".format(File.name.removesuffix(".md"), NotesPath.joinpath(Dir).joinpath(File.name).relative_to(NotesPath).as_posix().replace(" ", "%20")))

OutputFile = open(SummaryFilePath, "w")
OutputFile.write("[Cyberclopaedia](index.md)\n")

for NotesDir in NotesDirectoryList:
    SummariseDirectoryRecursively(NotesDir, OutputFile)

