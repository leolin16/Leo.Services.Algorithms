#%% basic
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janevay"

print(captains["Voyager"])

#%% get element
print(captains.get("Enterprise"))
print(captains.get("leo"))
#%% key iteration
for ship in captains:
    print(ship + ": " + captains[ship])

#%%
