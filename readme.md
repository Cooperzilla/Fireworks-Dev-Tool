# Fireworks Multi-Language Running

This project allows you to run/compile multiple languages together and use all their benefits

you configure the run.yaml to use, examples and docs are in example_run.yaml

***this project helps most with windows but some linux support***

<details>
<summary>List of supported languages</summary>

>- Python - executing
>- Ruby - executing
>- Php - executing
>- Js - executing
>- Java - executing and compiling to jar
>- Kotlin - executing and compiling to jar
>- Lua - executing
>- R - executing
>- Perl - executing
>- Julia - executing
>- Batch - executing
>- Powershell - executing
>- Dart - executing and compiling to exe, js, and linux executable
>- Go - executing and compiling to exe
>- C - compiling to exe
>- C++ - compiling to exe
>- Rust - compiling to exe
>- D - compiling to exe
>- Swift - compiling to exe
>- F# - executing and compiling to exe
>- C# - compiling to exe and dll
>- Objective-C - compiling to exe
>- Makefile - executing
>- Scala - executing and compiling to exe
>- Groovy - executing and compiling to jar
>- Clojure - executing and compiling to jar
>- Sass/Scss - compiling to css
>- Less - compiling to css
>- Stylus - compiling to css
>- Coffeescript - compiling to js
>- Typescript - compiling to Js and executing

List of supported executables

>- Jar(Java)
>- Exe(Windows)
>- Dll(dotnet)
</details>

<details>
<summary>Example Yaml</summary>

```yaml
execute:
    # examples with python
  - ["python", "file.py"] # main syntax
  - ["py", "file"] # alternative syntax NOT PUTTING FILE EXTENSION MAY NOT WORK
  - ["python", "folder/file.py"] # files in folders work too

    # supported languages
  - ["python", "file.py"] # py or python
  - ["ruby", "file.rb"] # rb or ruby
  - ["php", "file.php"]
  - ["js", "file.js"] # js, ,javascript or node
  - ["java", "file.jar"] # java or jar
  - ["lua", "file.lua"]
  - ["R", "file.r"] # R or r
  - ["perl", "file.pl"] # perl or pl
  - ["julia", "file.jl"] # julia or jl
  - ["exe", "file.exe"]
  - ["kts", "file.kts"] # kts or kotlinscript
  - ["batch", "file.bat"] # batch or bat
  - ["cmd", "file.cmd"] # same as a bat file but slightly different
  - ["powershell", "file.ps1"] # powershell, ps1 or ps
  - ["dart", "file.dart"]
  - ["go", "file.go"]
  - ["f#", "file.fs"] # f# or fs
  - ["dotnet", "file.dll"] # .net, dotnet, or dll
  - ["scala", "file.sc"] # scala or sc
  - ["java", "file.java"]
  - ["groovy", "file.groovy"]
  - ["clojure", "file.clj"] # clojure or clj
  - ["typescript", "file.ts"] # typescript or ts REQUIRES ts-node npm library
  - ["make"] # make or Make requires a MAKEFILE

compile:
    # supported languages
  - ["java", "file.java"]
  - ["c", "file.c"]
  - ["kotlin", "file.kt"] # kotlin or kt if making module use ktlib or kotlinlib
  - ["c++", "file.cpp"] # c++ or cpp
  - ["dartexe", "file.dart"] # dartexe for window,s dartjs for web, or dartnative for linux
  - ["go", "file.go"]
  - ["rust", "file.rs"] # rust or rs
  - ["swift", "file.swift"]
  - ["f#", "file.fs"] # f# or fs
  - ["D", "file.d"] # D or d
  - ["c#", "file.cs"] # c#, cs, c#exe, or csexe for exe or for dll c#dll or csdll
  - ["obj-c", "file.m"] # objective-c, objectivec, obj-c, and objc
  - ["scala", "file.scala"] # scala or sc
  - ["java", "file.java"]
  - ["groovy", "file.groovy"]
  - ["clojure", "file.clj"] # clojure or clj
  - ["sass", "file.sass"] # sass for a .sass file or scss for a .scss file
  - ["less", "file.less"]
  - ["stylus", "file.styl"] # stylus or styl
  - ["coffeescript", "file.coffee"] # coffeescript or coffee
  - ["typescript", "file.ts"] # typescript or ts


config: # optional
  js: "node" # put in name of cli of your js environment node is popular
  c: "gcc" # put in name of cli of your c compiler gnu gcc is popular for c/objective-c
  cpp: "g++" # put in name of cli of your c++ compiler gnu g++ is popular for c++/objective-c++
  d: "dmd" # put in name of cli of your D compiler dmd is popular
```
</details>
