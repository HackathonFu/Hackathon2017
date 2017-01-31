def main():
    f = open("data/dc.in","r")
    number_of_rows,number_of_slots,unavaible_slots,number_of_pools,number_of_server = f.readline().split(" ")
    #TODO: Parse into int to avoid later parsing
    lines = f.read().splitlines()
    unavaible_slot_list = []
    for unavaible_slot in range(int(unavaible_slots)):
        #r for row , s for which slot in current row
         r,s = lines[unavaible_slot].split(" ")
         coordinate = (r,s)
         unavaible_slot_list.append(coordinate)
    server_capacity_list = []
    #print unavaible_slot_list
    for server_capacity in range(int(unavaible_slots),int(unavaible_slot)+int(number_of_server)+1):
         # s stands for slots_taken , c stands for capacity
         s,c = lines[server_capacity].split(" ")
         coordinate = (s,c)
         server_capacity_list.append(coordinate)
    #print server_capacity_list
    f.close()





if __name__ == "__main__":
    main()
