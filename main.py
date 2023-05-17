import subprocess
import yaml

with open("run.yaml", "rb") as f:
    data = yaml.load(f, Loader=yaml.Loader)


# config
try:
    js = data["config"]["js"]
except:
    js = "node"

try:
    c = data["config"]["c"]
except:
    c = "gcc"

try:
    cpp = data["config"]["cpp"]
except:
    cpp = "g++"

try:
    d = data["config"]["cpp"]
except:
    d = "dmd"

# compiling
try:
    for i in data["compile"]:
        language = i[0]
        match language:
            case "java":
                subprocess.run(["jar", "cvf", ((i[1] + '.jar') if not i[1].endswith('.java') else i[1].strip('.java')  + '.jar'), (i[1] if i[1].endswith('.java') else i[1]  + '.java')])
            case "c":
                subprocess.run([c, i[1] if i[1].endswith(".c") else (i[1] + ".c"), "-o", (i[1].strip(".c") + ".exe") if i.endswith(".c") else (i[1] + ".exe")])
            case "kotlin":
                subprocess.run(["kotlinc", i[1] if i[1].endswith(".kt") else (i[1] + ".kt"), "-include-runtime", "-d", (i[1].strip(".kt") + ".jar") if i.endswith(".jar") else (i[1] + ".jar")])
            case "kt":
                subprocess.run(["kotlinc", i[1] if i[1].endswith(".kt") else (i[1] + ".kt"), "-include-runtime", "-d", (i[1].strip(".kt") + ".jar") if i.endswith(".jar") else (i[1] + ".jar")])
            case "kotlinlib":
                subprocess.run(["kotlinc", i[1] if i[1].endswith(".kt") else (i[1] + ".kt"), "-d", (i[1].strip(".kt") + ".jar") if i.endswith(".jar") else (i[1] + ".jar")])
            case "ktlib":
                subprocess.run(["kotlinc", i[1] if i[1].endswith(".kt") else (i[1] + ".kt"), "-d", (i[1].strip(".kt") + ".jar") if i.endswith(".jar") else (i[1] + ".jar")])
            case "cpp":
                subprocess.run([cpp, i[1] if i[1].endswith(".cpp") else (i[1] + ".cpp"), "-o", (i[1].strip(".cpp") + ".exe") if i.endswith(".cpp") else (i[1] + ".exe")])
            case "c++":
                subprocess.run([cpp, i[1] if i[1].endswith(".cpp") else (i[1] + ".cpp"), "-o", (i[1].strip(".cpp") + ".exe") if i.endswith(".cpp") else (i[1] + ".exe")])
            case "dartexe":
                subprocess.run(["dart", "compile", "exe", i[1] if i[1].endswith(".dart") else (i[1] + ".dart"), "-o", (i[1].strip(".dart") + ".exe") if i.endswith(".dart") else (i[1] + ".exe")])
            case "dartjs":
                subprocess.run(["dart", "compile", "js", i[1] if i[1].endswith(".dart") else (i[1] + ".dart"), "-o", (i[1].strip(".dart") + ".js") if i.endswith(".dart") else (i[1] + ".js")])
            case "dartnative":
                subprocess.run(["dart2native", i[1] if i[1].endswith(".dart") else (i[1] + ".dart"), "-o", (i[1].strip(".dart") + ".bin") if i.endswith(".dart") else (i[1] + ".bin")])
            case "go":
                subprocess.run(["go", "build", i[1] if i[1].endswith(".go") else (i[1] + ".go")])
            case "rust":
                subprocess.run(["rustc", i[1] if i[1].endswith(".rs") else (i[1] + ".rs")])
            case "rs":
                subprocess.run(["rustc", i[1] if i[1].endswith(".rs") else (i[1] + ".rs")])
            case "swift":
                subprocess.run(["swiftc", i[1] if i[1].endswith(".swift") else (i[1] + ".swift")])
            case "f#":
                subprocess.run(["dotnet", "fsc", i[1] if i[1].endswith(".fs") else (i[1] + ".fs")])
            case "fs":
                subprocess.run(["dotnet", "fsc", i[1] if i[1].endswith(".fs") else (i[1] + ".fs")])
            case "d":
                subprocess.run([d, i[1] if i[1].endswith(".d") else (i[1] + ".d")])
            case "D":
                subprocess.run([d, i[1] if i[1].endswith(".d") else (i[1] + ".d")])
            case "c#":
                subprocess.run(["csc", ("/out:" + ((i[1].strip('.cs') + '.exe') if i[1].endswith('.cs') else (i[1] + '.exe'))), i[1] if i[1].endswith(".cs") else (i[1] + ".cs")])
            case "cs":
                subprocess.run(["csc", ("/out:" + ((i[1].strip('.cs') + '.exe') if i[1].endswith('.cs') else (i[1] + '.exe'))), i[1] if i[1].endswith(".cs") else (i[1] + ".cs")])
            case "c#exe":
                subprocess.run(["csc", ("/out:" + ((i[1].strip('.cs') + '.exe') if i[1].endswith('.cs') else (i[1] + '.exe'))), i[1] if i[1].endswith(".cs") else (i[1] + ".cs")])
            case "csexe":
                subprocess.run(["csc", ("/out:" + ((i[1].strip('.cs') + '.exe') if i[1].endswith('.cs') else (i[1] + '.exe'))), i[1] if i[1].endswith(".cs") else (i[1] + ".cs")])
            case "c#dll":
                subprocess.run(["csc", "/target:library", ("/out:" + ((i[1].strip('.cs') + '.dll') if i[1].endswith('.cs') else (i[1] + '.dll'))), i[1] if i[1].endswith(".cs") else (i[1] + ".cs")])
            case "csdll":
                subprocess.run(["csc", "/target:library", ("/out:" + ((i[1].strip('.cs') + '.dll') if i[1].endswith('.cs') else (i[1] + '.dll'))), i[1] if i[1].endswith(".cs") else (i[1] + ".cs")])
            case "objective-c":
                subprocess.run([c, "-framework", "Foundation", i[1] if i[1].endswith(".m") else (i[1] + ".m"), "-o", (i[1].strip(".m") + ".exe") if i.endswith(".m") else (i[1] + ".exe")])
            case "objectivec":
                subprocess.run([c, "-framework", "Foundation", i[1] if i[1].endswith(".m") else (i[1] + ".m"), "-o", (i[1].strip(".m") + ".exe") if i.endswith(".m") else (i[1] + ".exe")])
            case "obj-c":
                subprocess.run([c, "-framework", "Foundation", i[1] if i[1].endswith(".m") else (i[1] + ".m"), "-o", (i[1].strip(".m") + ".exe") if i.endswith(".m") else (i[1] + ".exe")])
            case "objc":
                subprocess.run([c, "-framework", "Foundation", i[1] if i[1].endswith(".m") else (i[1] + ".m"), "-o", (i[1].strip(".m") + ".exe") if i.endswith(".m") else (i[1] + ".exe")])
            case "scala":
                subprocess.run(["scalac", i[1] if i[1].endswith(".scala") else (i[1] + ".scala"), "-d", (i[1].strip(".scala") + ".jar") if i.endswith(".scala") else (i[1] + ".jar")])
            case "sc":
                subprocess.run(["scalac", i[1] if i[1].endswith(".scala") else (i[1] + ".scala"), "-d", (i[1].strip(".scala") + ".jar") if i.endswith(".scala") else (i[1] + ".jar")])
            case "groovy":
                subprocess.run(["groovyc", i[1] if i[1].endswith(".groovy") else (i[1] + ".groovy"), "-d", (i[1].strip(".groovy") + ".jar") if i.endswith(".groovy") else (i[1] + ".jar")])
            case "clojure":
                subprocess.run(["clojure", "-e", f"(compile '{i[1] if i[1].endswith('.clj') else (i[1] + '.clj')}')"])
                subprocess.run(["jar", "cf", (i[1].strip(".clj") + ".jar") if i.endswith(".clj") else (i[1] + ".jar"), (i[1].strip(".clj") + ".class") if i.endswith(".clj") else (i[1] + ".class")])
            case "clj":
                subprocess.run(["clojure", "-e", f"(compile '{i[1] if i[1].endswith('.clj') else (i[1] + '.clj')}')"])
                subprocess.run(["jar", "cf", (i[1].strip(".clj") + ".jar") if i.endswith(".clj") else (i[1] + ".jar"), (i[1].strip(".clj") + ".class") if i.endswith(".clj") else (i[1] + ".class")])
            case "sass":
                subprocess.run(["sass", "--watch", i[1] if i.endswith(".sass") else (i[1] + ".sass"), (i[1].strip(".sass") + ".css") if i.endswith(".sass") else (i[1] + ".css")])
            case "scss":
                subprocess.run(["scss", "--watch", i[1] if i.endswith(".sass") else (i[1] + ".sass"), (i[1].strip(".scss") + ".css") if i.endswith(".scss") else (i[1] + ".css")])
            case "less":
                subprocess.run(["lessc", i[1] if i.endswith(".less") else (i[1] + ".less"), (i[1].strip(".less") + ".css") if i.endswith(".less") else (i[1] + ".css")])
            case "stylus":
                subprocess.run(["stylus", "--compress", i[1] if i.endswith(".styl") else (i[1] + ".styl"), (i[1].strip(".styl") + ".css") if i.endswith(".styl") else (i[1] + ".css")])
            case "styl":
                subprocess.run(["stylus", "--compress", i[1] if i.endswith(".styl") else (i[1] + ".styl"), (i[1].strip(".styl") + ".css") if i.endswith(".styl") else (i[1] + ".css")])
            case "coffeescript":
                subpross.run(["coffee", "--compile", i[1] if i.endswith(".coffee") else (i[1] + ".coffee")])
            case "coffee":
                subpross.run(["coffee", "--compile", i[1] if i.endswith(".coffee") else (i[1] + ".coffee")])
            case "typescript":
                subprocess.run(["tsc",i[1] if i[1].endswith(".ts") else (i[1] + ".ts")])
            case "ts":
                subprocess.run(["tsc",i[1] if i[1].endswith(".ts") else (i[1] + ".ts")])

except:
    print("There was an error compiling or you just executed with no compiling")

# executing
try:
    for i in data["execute"]:
        language = i[0]
        match language:
            case "python":
                subprocess.run(["python", f"{i[1] if i[1].endswith('.py') else i[1]  + '.py'}"])
            case "py":
                subprocess.run(["python", f"{i[1] if i[1].endswith('.py') else i[1]  + '.py'}"])
            case "ruby":
                subprocess.run(["ruby", f"{i[1] if i[1].endswith('.rb') else i[1]  + '.rb'}"])
            case "rb":
                subprocess.run(["ruby", f"{i[1] if i[1].endswith('.rb') else i[1]  + '.rb'}"])
            case "php":
                subprocess.run(["php", f"{i[1] if i[1].endswith('.php') else i[1]  + '.php'}"])
            case "node":
                subprocess.run([js, f"{i[1] if i[1].endswith('.js') else i[1]  + '.js'}"])
            case "js":
                subprocess.run([js, f"{i[1] if i[1].endswith('.js') else i[1]  + '.js'}"])
            case "javascript":
                subprocess.run([js, f"{i[1] if i[1].endswith('.js') else i[1]  + '.js'}"])
            case "java":
                subprocess.run(["java", "-jar", f"{i[1] if i[1].endswith('.jar') else i[1]  + '.jar'}"])
            case "jar":
                subprocess.run(["java", "-jar", f"{i[1] if i[1].endswith('.jar') else i[1]  + '.jar'}"])
            case "lua":
                subprocess.run(["lua", i[1] if i[1].endswith(".lua") else (i[1] + ".lua")])
            case "R":
                subprocess.run(["Rscript", i[1] if i[1].endswith(".r") else (i[1] + ".r")])
            case "r":
                subprocess.run(["Rscript", i[1] if i[1].endswith(".r") else (i[1] + ".r")])
            case "perl":
                subprocess.run(["perl", i[1] if i[1].endswith(".r") else (i[1] + ".r")])
            case "pl":
                subprocess.run(["perl", i[1] if i[1].endswith(".r") else (i[1] + ".r")])
            case "julia":
                subprocess.run(["julia", i[1] if i[1].endswith(".jl") else (i[1] + ".jl")])
            case "jl":
                subprocess.run(["julia", i[1] if i[1].endswith(".jl") else (i[1] + ".jl")])
            case "exe":
                subprocess.run(["./" + (i[1] if i[1].endswith(".exe") else (i[1] + ".exe"))])
            case "kotlinscript":
                subprocess.run(["kotlinc", "-script", i[1] if i.endswith(".kts") else (i[1] + ".kts")])
            case "kts":
                subprocess.run(["kotlinc", "-script", i[1] if i.endswith(".kts") else (i[1] + ".kts")])
            case "batch":
                subprocess.run([i[1] if i[1].endswith(".bat") else (i[1] + ".bat")])
            case "bat":
                subprocess.run([i[1] if i[1].endswith(".bat") else (i[1] + ".bat")])
            case "cmd":
                subprocess.run([i[1] if i[1].endswith(".cmd") else (i[1] + ".cmd")])
            case "powershell":
                subprocess.run(["powershell", i[1] if i[1].endswith(".ps1") else (i[1] + ".ps1")])
            case "ps1":
                subprocess.run(["powershell", i[1] if i[1].endswith(".ps1") else (i[1] + ".ps1")])
            case "ps":
                subprocess.run(["powershell", i[1] if i[1].endswith(".ps1") else (i[1] + ".ps1")])
            case "dart":
                subprocess.run(["dart", "run", i[1] if i[1].endswith(".dart") else (i[1] + ".dart")])
            case "go":
                subprocess.run(["go", "run", i[1] if i[1].endswith(".go") else (i[1] + ".go")])
            case "f#":
                subprocess.run(["dotnet", "fsi", i[1] if i[1].endswith(".fs") else (i[1] + ".fs")])
            case "fs":
                subprocess.run(["dotnet", "fsi", i[1] if i[1].endswith(".fs") else (i[1] + ".fs")])
            case ".net":
                subprocess.run("dotnet", i[1] if i[1].endswith(".dll") else (i[1] + ".dll"))
            case "dotnet":
                subprocess.run("dotnet", i[1] if i[1].endswith(".dll") else (i[1] + ".dll"))
            case "dll":
                subprocess.run("dotnet", i[1] if i[1].endswith(".dll") else (i[1] + ".dll"))
            case "scala":
                subprocess.run(["scala-cli", i[1] if i[1].endswith(".sc") else (i[1] + ".sc")])
            case "sc":
                subprocess.run(["scala-cli", i[1] if i[1].endswith(".sc") else (i[1] + ".sc")])
            case "java":
                subprocess.run(["java", i[1] if i[1].endswith(".java") else (i[1] + ".java")])
            case "groovy":
                subprocess.run(["groovy", i[1] if i[1].endswith(".groovy") else (i[1] + ".groovy")])
            case "clojure":
                subprocess.run(["clojure", i[1] if i[1].endswith(".clj") else (i[1] + ".clj")])
            case "clj":
                subprocess.run(["clj", i[1] if i[1].endswith(".clj") else (i[1] + ".clj")])
            case "typescript": # requires ts-node package on npm
                subprocess.run(["ts-node", i[1] if i[1].endswith(".ts") else (i[1] + ".ts")])
            case "ts": # requires ts-node package on npm
                subprocess.run(["ts-node", i[1] if i[1].endswith(".ts") else (i[1] + ".ts")])
            case "make":
                subprocess.run(["make"])
            case "Make":
                subprocess.run(["make"])
except:
    print("There was an error executing or you just compiled with no execution")
