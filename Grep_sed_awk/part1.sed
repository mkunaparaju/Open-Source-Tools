#a
1,/chart-top250/d
#b
/<\/table>/,$d
#c
/<span name=".*" data-value=".*"><\/span>/d
#d
s/\,//g
#e
s/title=".*" >\(.*\)<\/a>/\1/p
#f
s/ *<span class="secondaryInfo">(\(.*\))<\/span>/\1/p
#g
s/      \([0-9]*\)\./\1/p
#h
s/ *<strong title="\(.*\) based on \(.*\) votes">.*<\/strong>/\1\n\2\n/p
