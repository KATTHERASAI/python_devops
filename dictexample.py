ec2_instances_info = [

{
    "name" : "instance1",
    "type" : "t2.micro",
    "state" : "running"
},
{
    "name" : "instance2",
    "type" : "t2.small",
    "state" : "stopped"

},
{
    "name" : "instance3",
    "type" : "t2.medium",
    "state"  : "running"

}
]

#print ec2 in normal way
print(ec2_instances_info[1]["name"],ec2_instances_info[1]["state"])
#using for loop to print all the ec2 instances info
# for i in range(len(ec2_instances_info)):
#     print(ec2_instances_info[i]["name"],ec2_instances_info[i]["type"],ec2_instances_info[i]["state"])

#Using defining a function to print ec2 instances inf
def print_selected_info():
    print(
        ec2_instances_info[1]["name"], ec2_instances_info[1]["state"],  # name and state of instance at index 1
        ec2_instances_info[2]["state"],  # state of instance at index 2
        ec2_instances_info[0]["type"]    # type of instance at index 0
    )

print_selected_info()