""" two products: widgets and gizmos
 Each widget weighs 75 g
 Each gizmos weighs 112 g
 read from user the no of widgets and gizmos
 compute and display the total weight"""

widgets = int(input("How many widgets? "))
gizmos = int(input("How many gizmos? "))

widget_weight = 75
gizmo_weight = 112

total_weight = widgets * widget_weight + gizmos * gizmo_weight

print("The total weight is: %d g" % total_weight)