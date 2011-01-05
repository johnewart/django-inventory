from django.contrib import admin

from inventory.models import Permission, \
                             ItemTemplate, Item, \
                             ItemGroup, RetiredItem, InRepairsItem, \
                             Person, Inventory, Location


admin.site.register(Permission)
admin.site.register(Location)
admin.site.register(ItemTemplate)
admin.site.register(Item)
admin.site.register(ItemGroup)
admin.site.register(RetiredItem)
admin.site.register(InRepairsItem)
admin.site.register(Person)
admin.site.register(Inventory)


