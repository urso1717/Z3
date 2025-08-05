# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bom(models.Model):
    bom_id = models.AutoField(primary_key=True, db_comment='Unique id for the BOM')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')
    bom_name = models.CharField(unique=True, max_length=50, db_comment='BOM name', verbose_name='Bom name' )

    class Meta:
        managed = False
        db_table = 'BOM'
        db_table_comment = 'Bill of materials'


class BomDocument(models.Model):
    bom_document_id = models.AutoField(primary_key=True, db_comment='Unique id for the relationship with the document')
    bom = models.ForeignKey(Bom, models.DO_NOTHING, db_comment='Foreign key to the owner of the document')
    document = models.ForeignKey('Document', models.DO_NOTHING, blank=True, null=True, db_comment='Foreign key to the document')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'BOM_DOCUMENT'
        unique_together = (('bom', 'document'),)
        db_table_comment = 'Relationship with the documents'


class BomComponent(models.Model):
    bom_component_id = models.AutoField(primary_key=True, db_comment='Unique id for the relationship between the BOM and the component')
    bom = models.ForeignKey(Bom, models.DO_NOTHING, db_comment='Foreign key link to the BOM')
    component = models.ForeignKey('Component', models.DO_NOTHING, db_comment='Foreign key link to the component')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'BOM_COMPONENT'
        unique_together = (('bom', 'component'),)
        db_table_comment = 'Relationship between Bill of materials and the manufaturers components'


class BomTree(models.Model):
    bom_tree_id = models.AutoField(primary_key=True, db_comment='Unique id for the BOM tree')
    bom = models.ForeignKey(Bom, models.DO_NOTHING, db_comment='Foreign key link to the bom table')
    parent_bom = models.ForeignKey(Bom, models.DO_NOTHING, related_name='bomtree_parent_bom_set', blank=True, null=True, db_comment='Foreign key link to the bom table record that is the parent of the link indicated by the parent bom')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'BOM_TREE'
        unique_together = (('parent_bom', 'bom'),)
        db_table_comment = 'Structure of BOMs'

class CadReference(models.Model):

    cad_reference_id = models.AutoField(primary_key=True, db_comment='Unique id for the CAD_REFERENCE tree')
    bom_component = models.ForeignKey(BomComponent, models.DO_NOTHING, db_comment='Foreign key link to the BOM_COMPONENT')
    reference_item = models.CharField(unique=False, max_length=45, db_comment='Reference item', verbose_name='Reference item' )
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')

    class Meta:
        managed = False
        db_table = 'CAD_REFERENCE'
        db_table_comment = 'Cad reference'

    def __str__(self):
        return self.reference_item
    
# class CadReference

class Component(models.Model):
    component_id = models.AutoField(primary_key=True, db_comment='Unique id for the component')
    component_class = models.ForeignKey('ComponentClass', models.DO_NOTHING, blank=True, null=True, db_comment="Foreign key link to the component's class")
    component_name = models.CharField(unique=True, max_length=50, db_comment='Unique component  name', verbose_name='Part #' )
    part_number = models.CharField(max_length=45, blank=True, null=True, db_comment='Part name for the component')
    component_type = models.CharField(max_length=45, blank=True, null=True, db_comment='Type of the component')
    component_value = models.CharField(max_length=45, blank=True, null=True, db_comment='Value of the component')
    rating = models.CharField(max_length=45, blank=True, null=True, db_comment='Rating')
    tolerance = models.CharField(max_length=45, blank=True, null=True, db_comment='Tolarance')
    max_temperature = models.IntegerField(blank=True, null=True, db_comment='Maximum temperature in Centigrades')
    min_temperature = models.IntegerField(blank=True, null=True, db_comment='Minimum temperature in Centigrades')
    component_size = models.CharField(max_length=64, blank=True, null=True, db_comment='Size of the component')
    pcb_footprint = models.CharField(max_length=128, blank=True, null=True, db_comment='PCB footprint - dimensions of the components footprint on a board')
    schematic_part = models.CharField(max_length=128, blank=True, null=True, db_comment='Schematic part')
    part_type = models.CharField(max_length=128, blank=True, null=True, db_comment='Part type')
    component_ndaa = models.CharField(max_length=16, blank=True, null=True, db_comment='NDAA identifier of the component')
    fit = models.CharField(max_length=16, blank=True, null=True, db_comment='FIT - fault in time of the component')
    fit_source = models.CharField(max_length=20, blank=True, null=True, db_comment='FIT Source - source of the components FIT')
    color = models.CharField(max_length=45, blank=True, null=True, db_comment='Color of the component')
    component_description = models.CharField(max_length=1000, blank=True, null=True, db_comment='Description of the component')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')

    class Meta:
        managed = False
        db_table = 'COMPONENT'
        db_table_comment = 'Basic components'

    def __str__(self):
        return self.component_name


class ComponentAttribute(models.Model):
    component_attribute_id = models.AutoField(primary_key=True, db_comment='Unique id for the component attribute')
    component_class = models.ForeignKey('ComponentClass', models.DO_NOTHING, db_comment='Foreign key link to ')
    component_attribue_order = models.CharField(max_length=45, blank=True, null=True)
    component_attribute_name = models.CharField(unique=True, max_length=50, db_comment='Unique product name')
    component_attribute_description = models.CharField(max_length=50, blank=True, null=True, db_comment='Description of the product - up to 2K')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'COMPONENT_ATTRIBUTE'
        db_table_comment = 'Attributes for components of a given class - only attributes in this list should be shown'


class ComponentClass(models.Model):
    component_class_id = models.AutoField(primary_key=True, db_comment='Unique id for the class of the components')
    component_class_name = models.CharField(unique=True, max_length=50, blank=True, null=True, db_comment='Class for the basic component - resistor, capacitor, etc')
    component_class_order = models.IntegerField(blank=True, null=True, db_comment='Order in which the class is displayed')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'COMPONENT_CLASS'
        db_table_comment = 'Holds the classes of components - resistors, capacitors, etc'

    def __str__(self):
        return self.component_class_name


class ComponentDocument(models.Model):
    component_document_id = models.AutoField(primary_key=True, db_comment='Unique id for the relationship with the document')
    component = models.ForeignKey(Component, models.DO_NOTHING, db_comment='Foreign key to the owner of the document')
    document = models.ForeignKey('Document', models.DO_NOTHING, blank=True, null=True, db_comment='Foreign key to the document')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'COMPONENT_DOCUMENT'
        unique_together = (('component', 'document'),)
        db_table_comment = 'Relationship with the documents'


class Document(models.Model):
    document_id = models.AutoField(primary_key=True, db_comment='Unique id for the product')
    document_name = models.CharField(max_length=200, blank=True, null=True)
    document_location = models.CharField(max_length=250, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'DOCUMENT'
        unique_together = (('document_location', 'document_name'),)
        db_table_comment = 'Documents stored in the application'


class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True, db_comment='Unique id for the manufacturer')
    manufacturer_name = models.CharField(unique=True, max_length=100, db_comment='Unique manufacturers name')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'MANUFACTURER'
        db_table_comment = 'Manufacturers '

    def __str__(self):
        return self.manufacturer_name


class ManufacturerComponent(models.Model):
    manufacturer_component_id = models.AutoField(primary_key=True, db_comment='Unique id for the manufacturers component')
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_comment='Foreign key link to manufacturer')
    component = models.ForeignKey(Component, models.DO_NOTHING, db_comment='Foreign key link to component')
    manufacturer_part_number = models.CharField(max_length=50, db_comment='Part number for the manufacturer')
    country_of_origin = models.CharField(max_length=50, blank=True, null=True, db_comment='Country of origin of the part')
    lifecycle_status = models.CharField(max_length=31, blank=True, null=True, db_comment='Status of component in the lifecycle')
    approval_status = models.CharField(max_length=9, blank=True, null=True, db_comment='Approval status of the component')
    last_time_buy = models.DateField(blank=True, null=True, db_comment='Lastdate when the component was bought')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'MANUFACTURER_COMPONENT'
        unique_together = (('manufacturer', 'component'),)
        db_table_comment = 'Manufacturers Components'

    def __str__(self):
        return "Part #: " + self.manufacturer_part_number 


class ManufacturerComponentDocument(models.Model):
    manufacturer_component_document_id = models.AutoField(primary_key=True, db_comment='Unique id for the relationship with the document')
    manufacturer_component = models.ForeignKey(ManufacturerComponent, models.DO_NOTHING, db_comment='Foreign key to the owner of the document')
    document = models.ForeignKey(Document, models.DO_NOTHING, blank=True, null=True, db_comment='Foreign key to the document')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'MANUFACTURER_COMPONENT_DOCUMENT'
        unique_together = (('manufacturer_component', 'document'),)
        db_table_comment = 'Relationship with the documents'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, db_comment='Unique id for the product')
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True, db_comment='Foreign key link to a category of the product')
    product_name = models.CharField(unique=True, max_length=7, db_comment='Unique product name')
    sku_status = models.CharField(max_length=8, blank=True, null=True, db_comment='Active or Inactive SKU')
    marketing_name = models.CharField(max_length=50, blank=True, null=True, db_comment='Name under which the product is marketed')
    product_description = models.CharField(max_length=1000, blank=True, null=True, db_comment='Description of the product')
    ndaa_product = models.CharField(max_length=45, blank=True, null=True, db_comment='NDAA identifier of the product')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'PRODUCT'
        db_table_comment = 'List of products'

    def __str__(self):
        return self.product_name + " (" + self.marketing_name + ")"


class ProductCategory(models.Model):
    product_category_id = models.AutoField(primary_key=True, db_comment='Unique id for the product category')
    product_category_name = models.CharField(unique=True, max_length=50, blank=True, null=True, db_comment='Name of the category of the product')
    product_category_order = models.IntegerField(blank=True, null=True, db_comment='Order of the category of the product, used for display')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'PRODUCT_CATEGORY'
        db_table_comment = 'Holds the categories of products'


class ProductDocument(models.Model):
    product_document_id = models.AutoField(primary_key=True, db_comment='Unique id for the relationship with the document')
    product = models.ForeignKey(Product, models.DO_NOTHING, db_comment='Foreign key to the owner of the document')
    document = models.ForeignKey(Document, models.DO_NOTHING, blank=True, null=True, db_comment='Foreign key to the document')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'PRODUCT_DOCUMENT'
        unique_together = (('product', 'document'),)
        db_table_comment = 'Relationship with the documents'


class ProductVersion(models.Model):
    product_version_id = models.AutoField(primary_key=True, db_comment='Unique id for the product version')
    product = models.ForeignKey(Product, models.DO_NOTHING, db_comment='Foreign key link to the product')
    bom = models.ForeignKey(Bom, models.DO_NOTHING, blank=True, null=True, db_comment='Foreign key link to the BOM')
    version_name = models.CharField(max_length=10, db_comment='Version of the product')
    version_status = models.CharField(max_length=17, db_comment='Status of the version')
    version_information = models.CharField(max_length=1000, blank=True, null=True, db_comment='Information about the version')
    version_reference = models.CharField(max_length=250, blank=True, null=True, db_comment='Reference of the version of the product')
    version_locked = models.IntegerField(db_comment='Is the version locked and cannot be edited')
    ndaa_version = models.CharField(max_length=45, blank=True, null=True, db_comment='NDAA identifier of the product version')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'PRODUCT_VERSION'
        unique_together = (('product', 'version_name'),)
        db_table_comment = 'Versions of products'

    def __str__(self):
        return str(self.product_version_id)


class ProductVersionDocument(models.Model):
    product_version_document_id = models.AutoField(primary_key=True, db_comment='Unique id for the relationship with the document')
    product_version = models.ForeignKey(ProductVersion, models.DO_NOTHING, db_comment='Foreign key to the owner of the document')
    document = models.ForeignKey(Document, models.DO_NOTHING, blank=True, null=True, db_comment='Foreign key to the document')
    user = models.ForeignKey('User', models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'PRODUCT_VERSION_DOCUMENT'
        unique_together = (('product_version', 'document'),)
        db_table_comment = 'Relationship with the documents'


class User(models.Model):
    user_id = models.AutoField(primary_key=True, db_comment='Unique id for the user')
    username = models.CharField(max_length=16, db_comment='Username used for logon')
    password = models.CharField(max_length=32, db_comment='Password used for logon, must be encrypted')
    last_name = models.CharField(max_length=100, db_comment='Last name of the user')
    first_name = models.CharField(max_length=100, db_comment='First name of the user')
    email = models.CharField(max_length=255, blank=True, null=True, db_comment='Email of the user')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'USER'
        db_table_comment = 'List of users'

    def __str__(self):
        return self.username


class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True, db_comment='Unique id for the vendor')
    vendor_name = models.CharField(unique=True, max_length=100, db_comment='Unique vendor name')
    vendor_address_line1 = models.CharField(max_length=200, blank=True, null=True, db_comment='Vendors address line 1')
    vendor_address_line2 = models.CharField(max_length=200, blank=True, null=True, db_comment='Vendors address line 2')
    vendor_address_city = models.CharField(max_length=45, blank=True, null=True, db_comment='Vendors city')
    vendor_address_state = models.CharField(max_length=2, blank=True, null=True, db_comment='Vendors state')
    vendor_address_zip = models.CharField(max_length=5, blank=True, null=True, db_comment='Vendors ZIP')
    vendor_email = models.CharField(max_length=45, blank=True, null=True, db_comment='VEndors email')
    vendor_phone = models.CharField(max_length=45, blank=True, null=True, db_comment='Vendors phone')
    vendor_information = models.CharField(max_length=1000, blank=True, null=True, db_comment='Additional vendors information')
    user = models.ForeignKey(User, models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'VENDOR'
        db_table_comment = 'Vendors'

    def __str__(self):
        return self.vendor_name

class VendorMfrComponent(models.Model):
    vendor_mfr_component_id = models.AutoField(primary_key=True, db_comment='Unique id for the relationship between the vendor and the manufaturers component')
    manufacturer_component = models.ForeignKey(ManufacturerComponent, models.DO_NOTHING, db_comment='Foreign key link to the manufactures component')
    vendor = models.ForeignKey(Vendor, models.DO_NOTHING, db_comment='Foreign key link to the Vendor')
    vendor_part_number = models.CharField(max_length=50, db_comment='Part number for the vendor')
    moq = models.CharField(max_length=45, blank=True, null=True, db_comment='Minimum Order Quantity')
    lead_time = models.CharField(max_length=45, blank=True, null=True, db_comment='Lead Time - duration needed to replenish the stock')
    currency = models.CharField(max_length=45, db_comment='Currency used to buy the component')
    user = models.ForeignKey(User, models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'VENDOR_MFR_COMPONENT'
        unique_together = (('vendor', 'manufacturer_component'),)
        db_table_comment = 'Vendor association with a manufactor component'

    def __str__(self):
        return "Part #: " + self.vendor_part_number + ", vendor: " + str( self.vendor )


class VendorMfrComponentDocument(models.Model):
    vendor_mfr_component_document_id = models.AutoField(primary_key=True, db_comment='Unique id for the relationship with the document')
    vendor_mfr_component = models.ForeignKey(VendorMfrComponent, models.DO_NOTHING, db_comment='Foreign key to the owner of the document')
    document = models.ForeignKey(Document, models.DO_NOTHING, blank=True, null=True, db_comment='Foreign key to the document')
    user = models.ForeignKey(User, models.DO_NOTHING, db_comment='Id (foreign key) of the user table, corresponding to last user to update the table')
    update_time = models.DateTimeField(db_comment='Timestamp of the last update, default to current timestamp')

    class Meta:
        managed = False
        db_table = 'VENDOR_MFR_COMPONENT_DOCUMENT'
        unique_together = (('vendor_mfr_component', 'document'),)
        db_table_comment = 'Relationship with the documents'
