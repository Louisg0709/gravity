extends Node2D

#factors to multiply mass by
const mm=7.35*pow(10,22)  # moon massunits 
const planetm=5.97*pow(10,24)
#const starm=1.989*pow(10,30)

func _ready():
	$earth.mass=planetm
	$moon.mass=mm
	#$sun.mass=starm
