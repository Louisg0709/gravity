extends Node2D

@export var target = ""
@onready var body = get_parent().get_node(target)

var acceleration
@export var mass = 100
@export var velocity = Vector2(0,0)
var force = Vector2(0,0)
const G = 6.67*pow(10,-11)



var timestep = 1

func calculate_force(body):
	var dist = position.distance_to(body.position)
	var forcemag=G*mass*body.mass/pow(dist,2)
	force.x=(forcemag/dist)*(body.position.x-position.x)
	force.y=(forcemag/dist)*(body.position.y-position.y)   
	return force
   
func calculate_acceleration(force):
	var ax = force.x/mass
	var ay = force.y/mass
	acceleration = Vector2(ax,ay)
	return acceleration

func calculate_new_velocity(body):
	acceleration = calculate_acceleration(calculate_force(body))
	var new_velocity = velocity + timestep*acceleration
	return new_velocity

# Called when the node enters the scene tree for the first time.
func _ready():
	#mass = mass * mmunits
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func physics_process(delta):
	velocity = calculate_new_velocity(body)
	position+=timestep*velocity
