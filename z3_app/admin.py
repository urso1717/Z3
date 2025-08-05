from django.contrib import admin
from .models import Bom
from .models import BomDocument
from .models import BomComponent
from .models import BomTree
# from .models import BomSubassembly
from .models import Component
from .models import ComponentAttribute
from .models import ComponentClass
from .models import ComponentDocument
from .models import Document
# from .models import ComponentCategory
from .models import Manufacturer
from .models import ManufacturerComponent
from .models import ManufacturerComponentDocument
from .models import Product
from .models import ProductCategory
from .models import ProductVersion
from .models import ProductVersionDocument
# from .models import ProductVersionTree
from .models import User
from .models import Vendor
from .models import VendorMfrComponent
from .models import VendorMfrComponentDocument

class BomAdmin( admin.ModelAdmin ):
    exclude = ["bom_id", "update_time"]
 
class BomDocumentAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class BomComponentAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class BomTreeAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class ComponentAdmin( admin.ModelAdmin ):
    exclude = ["update_time", "part_number"]
 
class ComponentClassAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class ComponentAttributeAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class ComponentDocumentAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class DocumentAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class ManufacturerAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class ManufacturerComponentAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class ManufacturerComponentDocumentAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class ProductCategoryAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class ProductVersionDocumentAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class ProductVersionAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class ProductAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class UserAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class VendorMfrComponentAdmin( admin.ModelAdmin ):
    exclude = ["update_time"]
 
class VendorMfrComponentDocumentAdmin( admin.ModelAdmin ):
    # readonly_fields = ["update_time"]
    exclude = ('update_time', )
 
admin.site.register(Bom, BomAdmin)
admin.site.register(BomDocument, BomDocumentAdmin)
admin.site.register(BomComponent, BomComponentAdmin)
admin.site.register(BomTree, BomTreeAdmin)
# admin.site.register(BomSubassembly)
admin.site.register(Component, ComponentAdmin)
admin.site.register(ComponentClass, ComponentClassAdmin)
admin.site.register(ComponentDocument, ComponentDocumentAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(ComponentAttribute, ComponentAttributeAdmin)
# admin.site.register(ComponentCategory)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(ManufacturerComponent, ManufacturerComponentAdmin)
admin.site.register(ManufacturerComponentDocument, ManufacturerComponentDocumentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductVersion, ProductVersionAdmin)
admin.site.register(ProductVersionDocument, ProductVersionDocumentAdmin)
# admin.site.register(ProductVersionTree)
admin.site.register(User, UserAdmin)
admin.site.register(Vendor)
admin.site.register(VendorMfrComponent, VendorMfrComponentAdmin)
admin.site.register(VendorMfrComponentDocument, VendorMfrComponentDocumentAdmin)


