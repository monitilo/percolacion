#!bin/bash


start=$(date +%s)
for n in {4,8,16,32,64,128}
do
	
	mkdir "L$n/"
	
	for r in {1..50}
	do
		p=$(bc -l <<< "$r*0.01" )
		echo $(./test.e $n $p)
		mv *.txt "L$n/"
	done
	
	for r in {1..2000}
	do
		p=$(bc -l <<< "$r*0.0001 + 0.5" )
		echo $(./test.e $n $p)
		mv *.txt "L$n/"
	done

	for r in {1..29}
	do
		p=$(bc -l <<< "$r*0.01 + 0.7" )
		echo $(./test.e $n $p)
		mv *.txt "L$n/"
	done

		

done

end=$(date +%s)

echo $(($end-$start))
