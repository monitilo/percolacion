#!bin/bash


start=$(date +%s)
for n in {4,8,16,32,64,128}
do
	
	mkdir "L=$n/"
	
	for r in {1..50}
	do
		p=$(bc -l <<< "$r*0.01" )
		echo $(./test.e $n $p)
	done
	
	for r in {1..100}
	do
		p=$(bc -l <<< "$r*0.002 + 0.5" )
		echo $(./test.e $n $p)
	done

	for r in {1..29}
	do
		p=$(bc -l <<< "$r*0.01 + 0.7" )
		echo $(./test.e $n $p)
	done
	mv *.txt "L=$n/"
		

done

end=$(date +%s)

echo $(($end-$start))
