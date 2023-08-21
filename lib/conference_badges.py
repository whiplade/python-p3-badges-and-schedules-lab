def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badge_names = []
    for name in names:
        badge_names.append(f'Hello, my name is {name}.')
    return badge_names

def assign_rooms(names):
    rooms = range(1, 9)
    room_numbers = []

    for index, name in enumerate(names):
        room_number = rooms[index]
        room_numbers.append(f'Hello, {name}! You\'ll be assigned to room {room_number}!')
    return room_numbers

def printer(names):
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for message in badge_messages:
        print(message)
    
    for assignment in room_assignments:
        print(assignment)
