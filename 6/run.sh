#!bin/bash


start=$(date +%s)
n=32

for r in {0..1000}
do
	p=$(bc -l <<< "$r*0.0003+0.4" )
	echo $(./test.e $n $p)
done
	

end=$(date +%s)

echo $(($end-$start))
