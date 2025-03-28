[Skip to content](https://fastapi.tiangolo.com/reference/openapi/models/#openapi-models)

# OpenAPI `models` [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#openapi-models "Permanent link")

OpenAPI Pydantic models used to generate and validate the generated OpenAPI.

## `` fastapi.openapi.models [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models "Permanent link")

### `` SchemaOrBool`module-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SchemaOrBool "Permanent link")

```
SchemaOrBool = Union[Schema, bool]

```

### `` SecurityScheme`module-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecurityScheme "Permanent link")

```
SecurityScheme = Union[\
    APIKey, HTTPBase, OAuth2, OpenIdConnect, HTTPBearer\
]

```

### `` BaseModelWithConfig [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.BaseModelWithConfig "Permanent link")

Bases: `BaseModel`

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.BaseModelWithConfig.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.BaseModelWithConfig.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.BaseModelWithConfig.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Contact [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Contact "Permanent link")

Bases: `BaseModelWithConfig`

#### `` name`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Contact.name "Permanent link")

```
name = None

```

#### `` url`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Contact.url "Permanent link")

```
url = None

```

#### `` email`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Contact.email "Permanent link")

```
email = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Contact.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Contact.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Contact.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` License [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.License "Permanent link")

Bases: `BaseModelWithConfig`

#### `` name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.License.name "Permanent link")

```
name

```

#### `` identifier`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.License.identifier "Permanent link")

```
identifier = None

```

#### `` url`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.License.url "Permanent link")

```
url = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.License.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.License.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.License.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Info [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Info "Permanent link")

Bases: `BaseModelWithConfig`

#### `` title`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Info.title "Permanent link")

```
title

```

#### `` summary`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Info.summary "Permanent link")

```
summary = None

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Info.description "Permanent link")

```
description = None

```

#### `` termsOfService`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Info.termsOfService "Permanent link")

```
termsOfService = None

```

#### `` contact`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Info.contact "Permanent link")

```
contact = None

```

#### `` license`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Info.license "Permanent link")

```
license = None

```

#### `` version`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Info.version "Permanent link")

```
version

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Info.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Info.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Info.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` ServerVariable [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ServerVariable "Permanent link")

Bases: `BaseModelWithConfig`

#### `` enum`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ServerVariable.enum "Permanent link")

```
enum = None

```

#### `` default`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ServerVariable.default "Permanent link")

```
default

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ServerVariable.description "Permanent link")

```
description = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ServerVariable.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ServerVariable.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ServerVariable.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Server [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Server "Permanent link")

Bases: `BaseModelWithConfig`

#### `` url`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Server.url "Permanent link")

```
url

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Server.description "Permanent link")

```
description = None

```

#### `` variables`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Server.variables "Permanent link")

```
variables = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Server.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Server.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Server.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Reference [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Reference "Permanent link")

Bases: `BaseModel`

#### `` ref`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Reference.ref "Permanent link")

```
ref = Field(alias='$ref')

```

### `` Discriminator [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Discriminator "Permanent link")

Bases: `BaseModel`

#### `` propertyName`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Discriminator.propertyName "Permanent link")

```
propertyName

```

#### `` mapping`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Discriminator.mapping "Permanent link")

```
mapping = None

```

### `` XML [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.XML "Permanent link")

Bases: `BaseModelWithConfig`

#### `` name`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.XML.name "Permanent link")

```
name = None

```

#### `` namespace`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.XML.namespace "Permanent link")

```
namespace = None

```

#### `` prefix`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.XML.prefix "Permanent link")

```
prefix = None

```

#### `` attribute`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.XML.attribute "Permanent link")

```
attribute = None

```

#### `` wrapped`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.XML.wrapped "Permanent link")

```
wrapped = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.XML.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.XML.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.XML.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` ExternalDocumentation [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ExternalDocumentation "Permanent link")

Bases: `BaseModelWithConfig`

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ExternalDocumentation.description "Permanent link")

```
description = None

```

#### `` url`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ExternalDocumentation.url "Permanent link")

```
url

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ExternalDocumentation.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ExternalDocumentation.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ExternalDocumentation.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Schema [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema "Permanent link")

Bases: `BaseModelWithConfig`

#### `` schema\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.schema_ "Permanent link")

```
schema_ = Field(default=None, alias='$schema')

```

#### `` vocabulary`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.vocabulary "Permanent link")

```
vocabulary = Field(default=None, alias='$vocabulary')

```

#### `` id`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.id "Permanent link")

```
id = Field(default=None, alias='$id')

```

#### `` anchor`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.anchor "Permanent link")

```
anchor = Field(default=None, alias='$anchor')

```

#### `` dynamicAnchor`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.dynamicAnchor "Permanent link")

```
dynamicAnchor = Field(default=None, alias='$dynamicAnchor')

```

#### `` ref`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.ref "Permanent link")

```
ref = Field(default=None, alias='$ref')

```

#### `` dynamicRef`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.dynamicRef "Permanent link")

```
dynamicRef = Field(default=None, alias='$dynamicRef')

```

#### `` defs`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.defs "Permanent link")

```
defs = Field(default=None, alias='$defs')

```

#### `` comment`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.comment "Permanent link")

```
comment = Field(default=None, alias='$comment')

```

#### `` allOf`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.allOf "Permanent link")

```
allOf = None

```

#### `` anyOf`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.anyOf "Permanent link")

```
anyOf = None

```

#### `` oneOf`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.oneOf "Permanent link")

```
oneOf = None

```

#### `` not\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.not_ "Permanent link")

```
not_ = Field(default=None, alias='not')

```

#### `` if\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.if_ "Permanent link")

```
if_ = Field(default=None, alias='if')

```

#### `` then`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.then "Permanent link")

```
then = None

```

#### `` else\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.else_ "Permanent link")

```
else_ = Field(default=None, alias='else')

```

#### `` dependentSchemas`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.dependentSchemas "Permanent link")

```
dependentSchemas = None

```

#### `` prefixItems`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.prefixItems "Permanent link")

```
prefixItems = None

```

#### `` items`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.items "Permanent link")

```
items = None

```

#### `` contains`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.contains "Permanent link")

```
contains = None

```

#### `` properties`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.properties "Permanent link")

```
properties = None

```

#### `` patternProperties`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.patternProperties "Permanent link")

```
patternProperties = None

```

#### `` additionalProperties`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.additionalProperties "Permanent link")

```
additionalProperties = None

```

#### `` propertyNames`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.propertyNames "Permanent link")

```
propertyNames = None

```

#### `` unevaluatedItems`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.unevaluatedItems "Permanent link")

```
unevaluatedItems = None

```

#### `` unevaluatedProperties`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.unevaluatedProperties "Permanent link")

```
unevaluatedProperties = None

```

#### `` type`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.type "Permanent link")

```
type = None

```

#### `` enum`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.enum "Permanent link")

```
enum = None

```

#### `` const`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.const "Permanent link")

```
const = None

```

#### `` multipleOf`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.multipleOf "Permanent link")

```
multipleOf = Field(default=None, gt=0)

```

#### `` maximum`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.maximum "Permanent link")

```
maximum = None

```

#### `` exclusiveMaximum`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.exclusiveMaximum "Permanent link")

```
exclusiveMaximum = None

```

#### `` minimum`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.minimum "Permanent link")

```
minimum = None

```

#### `` exclusiveMinimum`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.exclusiveMinimum "Permanent link")

```
exclusiveMinimum = None

```

#### `` maxLength`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.maxLength "Permanent link")

```
maxLength = Field(default=None, ge=0)

```

#### `` minLength`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.minLength "Permanent link")

```
minLength = Field(default=None, ge=0)

```

#### `` pattern`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.pattern "Permanent link")

```
pattern = None

```

#### `` maxItems`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.maxItems "Permanent link")

```
maxItems = Field(default=None, ge=0)

```

#### `` minItems`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.minItems "Permanent link")

```
minItems = Field(default=None, ge=0)

```

#### `` uniqueItems`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.uniqueItems "Permanent link")

```
uniqueItems = None

```

#### `` maxContains`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.maxContains "Permanent link")

```
maxContains = Field(default=None, ge=0)

```

#### `` minContains`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.minContains "Permanent link")

```
minContains = Field(default=None, ge=0)

```

#### `` maxProperties`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.maxProperties "Permanent link")

```
maxProperties = Field(default=None, ge=0)

```

#### `` minProperties`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.minProperties "Permanent link")

```
minProperties = Field(default=None, ge=0)

```

#### `` required`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.required "Permanent link")

```
required = None

```

#### `` dependentRequired`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.dependentRequired "Permanent link")

```
dependentRequired = None

```

#### `` format`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.format "Permanent link")

```
format = None

```

#### `` contentEncoding`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.contentEncoding "Permanent link")

```
contentEncoding = None

```

#### `` contentMediaType`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.contentMediaType "Permanent link")

```
contentMediaType = None

```

#### `` contentSchema`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.contentSchema "Permanent link")

```
contentSchema = None

```

#### `` title`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.title "Permanent link")

```
title = None

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.description "Permanent link")

```
description = None

```

#### `` default`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.default "Permanent link")

```
default = None

```

#### `` deprecated`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.deprecated "Permanent link")

```
deprecated = None

```

#### `` readOnly`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.readOnly "Permanent link")

```
readOnly = None

```

#### `` writeOnly`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.writeOnly "Permanent link")

```
writeOnly = None

```

#### `` examples`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.examples "Permanent link")

```
examples = None

```

#### `` discriminator`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.discriminator "Permanent link")

```
discriminator = None

```

#### `` xml`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.xml "Permanent link")

```
xml = None

```

#### `` externalDocs`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.externalDocs "Permanent link")

```
externalDocs = None

```

#### `` example`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.example "Permanent link")

```
example = None

```

Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Schema.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Example [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Example "Permanent link")

Bases: `TypedDict`

#### `` summary`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Example.summary "Permanent link")

```
summary

```

#### `` description`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Example.description "Permanent link")

```
description

```

#### `` value`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Example.value "Permanent link")

```
value

```

#### `` externalValue`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Example.externalValue "Permanent link")

```
externalValue

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Example.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Example.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` ParameterInType [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterInType "Permanent link")

Bases: `Enum`

#### `` query`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterInType.query "Permanent link")

```
query = 'query'

```

#### `` header`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterInType.header "Permanent link")

```
header = 'header'

```

#### `` path`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterInType.path "Permanent link")

```
path = 'path'

```

#### `` cookie`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterInType.cookie "Permanent link")

```
cookie = 'cookie'

```

### `` Encoding [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Encoding "Permanent link")

Bases: `BaseModelWithConfig`

#### `` contentType`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Encoding.contentType "Permanent link")

```
contentType = None

```

#### `` headers`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Encoding.headers "Permanent link")

```
headers = None

```

#### `` style`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Encoding.style "Permanent link")

```
style = None

```

#### `` explode`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Encoding.explode "Permanent link")

```
explode = None

```

#### `` allowReserved`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Encoding.allowReserved "Permanent link")

```
allowReserved = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Encoding.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Encoding.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Encoding.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` MediaType [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.MediaType "Permanent link")

Bases: `BaseModelWithConfig`

#### `` schema\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.MediaType.schema_ "Permanent link")

```
schema_ = Field(default=None, alias='schema')

```

#### `` example`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.MediaType.example "Permanent link")

```
example = None

```

#### `` examples`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.MediaType.examples "Permanent link")

```
examples = None

```

#### `` encoding`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.MediaType.encoding "Permanent link")

```
encoding = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.MediaType.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.MediaType.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.MediaType.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` ParameterBase [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase "Permanent link")

Bases: `BaseModelWithConfig`

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.description "Permanent link")

```
description = None

```

#### `` required`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.required "Permanent link")

```
required = None

```

#### `` deprecated`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.deprecated "Permanent link")

```
deprecated = None

```

#### `` style`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.style "Permanent link")

```
style = None

```

#### `` explode`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.explode "Permanent link")

```
explode = None

```

#### `` allowReserved`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.allowReserved "Permanent link")

```
allowReserved = None

```

#### `` schema\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.schema_ "Permanent link")

```
schema_ = Field(default=None, alias='schema')

```

#### `` example`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.example "Permanent link")

```
example = None

```

#### `` examples`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.examples "Permanent link")

```
examples = None

```

#### `` content`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.content "Permanent link")

```
content = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.ParameterBase.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Parameter [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter "Permanent link")

Bases: `ParameterBase`

#### `` name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.name "Permanent link")

```
name

```

#### `` in\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.in_ "Permanent link")

```
in_ = Field(alias='in')

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.description "Permanent link")

```
description = None

```

#### `` required`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.required "Permanent link")

```
required = None

```

#### `` deprecated`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.deprecated "Permanent link")

```
deprecated = None

```

#### `` style`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.style "Permanent link")

```
style = None

```

#### `` explode`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.explode "Permanent link")

```
explode = None

```

#### `` allowReserved`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.allowReserved "Permanent link")

```
allowReserved = None

```

#### `` schema\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.schema_ "Permanent link")

```
schema_ = Field(default=None, alias='schema')

```

#### `` example`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.example "Permanent link")

```
example = None

```

#### `` examples`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.examples "Permanent link")

```
examples = None

```

#### `` content`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.content "Permanent link")

```
content = None

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Parameter.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Header [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header "Permanent link")

Bases: `ParameterBase`

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.description "Permanent link")

```
description = None

```

#### `` required`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.required "Permanent link")

```
required = None

```

#### `` deprecated`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.deprecated "Permanent link")

```
deprecated = None

```

#### `` style`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.style "Permanent link")

```
style = None

```

#### `` explode`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.explode "Permanent link")

```
explode = None

```

#### `` allowReserved`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.allowReserved "Permanent link")

```
allowReserved = None

```

#### `` schema\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.schema_ "Permanent link")

```
schema_ = Field(default=None, alias='schema')

```

#### `` example`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.example "Permanent link")

```
example = None

```

#### `` examples`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.examples "Permanent link")

```
examples = None

```

#### `` content`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.content "Permanent link")

```
content = None

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Header.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` RequestBody [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.RequestBody "Permanent link")

Bases: `BaseModelWithConfig`

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.RequestBody.description "Permanent link")

```
description = None

```

#### `` content`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.RequestBody.content "Permanent link")

```
content

```

#### `` required`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.RequestBody.required "Permanent link")

```
required = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.RequestBody.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.RequestBody.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.RequestBody.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Link [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Link "Permanent link")

Bases: `BaseModelWithConfig`

#### `` operationRef`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Link.operationRef "Permanent link")

```
operationRef = None

```

#### `` operationId`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Link.operationId "Permanent link")

```
operationId = None

```

#### `` parameters`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Link.parameters "Permanent link")

```
parameters = None

```

#### `` requestBody`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Link.requestBody "Permanent link")

```
requestBody = None

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Link.description "Permanent link")

```
description = None

```

#### `` server`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Link.server "Permanent link")

```
server = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Link.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Link.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Link.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Response [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Response "Permanent link")

Bases: `BaseModelWithConfig`

#### `` description`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Response.description "Permanent link")

```
description

```

#### `` headers`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Response.headers "Permanent link")

```
headers = None

```

#### `` content`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Response.content "Permanent link")

```
content = None

```

#### `` links`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Response.links "Permanent link")

```
links = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Response.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Response.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Response.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Operation [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation "Permanent link")

Bases: `BaseModelWithConfig`

#### `` tags`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.tags "Permanent link")

```
tags = None

```

#### `` summary`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.summary "Permanent link")

```
summary = None

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.description "Permanent link")

```
description = None

```

#### `` externalDocs`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.externalDocs "Permanent link")

```
externalDocs = None

```

#### `` operationId`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.operationId "Permanent link")

```
operationId = None

```

#### `` parameters`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.parameters "Permanent link")

```
parameters = None

```

#### `` requestBody`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.requestBody "Permanent link")

```
requestBody = None

```

#### `` responses`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.responses "Permanent link")

```
responses = None

```

#### `` callbacks`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.callbacks "Permanent link")

```
callbacks = None

```

#### `` deprecated`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.deprecated "Permanent link")

```
deprecated = None

```

#### `` security`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.security "Permanent link")

```
security = None

```

#### `` servers`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.servers "Permanent link")

```
servers = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Operation.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` PathItem [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem "Permanent link")

Bases: `BaseModelWithConfig`

#### `` ref`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.ref "Permanent link")

```
ref = Field(default=None, alias='$ref')

```

#### `` summary`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.summary "Permanent link")

```
summary = None

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.description "Permanent link")

```
description = None

```

#### `` get`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.get "Permanent link")

```
get = None

```

#### `` put`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.put "Permanent link")

```
put = None

```

#### `` post`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.post "Permanent link")

```
post = None

```

#### `` delete`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.delete "Permanent link")

```
delete = None

```

#### `` options`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.options "Permanent link")

```
options = None

```

#### `` head`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.head "Permanent link")

```
head = None

```

#### `` patch`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.patch "Permanent link")

```
patch = None

```

#### `` trace`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.trace "Permanent link")

```
trace = None

```

#### `` servers`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.servers "Permanent link")

```
servers = None

```

#### `` parameters`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.parameters "Permanent link")

```
parameters = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.PathItem.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` SecuritySchemeType [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecuritySchemeType "Permanent link")

Bases: `Enum`

#### `` apiKey`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecuritySchemeType.apiKey "Permanent link")

```
apiKey = 'apiKey'

```

#### `` http`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecuritySchemeType.http "Permanent link")

```
http = 'http'

```

#### `` oauth2`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecuritySchemeType.oauth2 "Permanent link")

```
oauth2 = 'oauth2'

```

#### `` openIdConnect`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecuritySchemeType.openIdConnect "Permanent link")

```
openIdConnect = 'openIdConnect'

```

### `` SecurityBase [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecurityBase "Permanent link")

Bases: `BaseModelWithConfig`

#### `` type\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecurityBase.type_ "Permanent link")

```
type_ = Field(alias='type')

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecurityBase.description "Permanent link")

```
description = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecurityBase.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecurityBase.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.SecurityBase.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` APIKeyIn [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKeyIn "Permanent link")

Bases: `Enum`

#### `` query`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKeyIn.query "Permanent link")

```
query = 'query'

```

#### `` header`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKeyIn.header "Permanent link")

```
header = 'header'

```

#### `` cookie`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKeyIn.cookie "Permanent link")

```
cookie = 'cookie'

```

### `` APIKey [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKey "Permanent link")

Bases: `SecurityBase`

#### `` type\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKey.type_ "Permanent link")

```
type_ = Field(default=apiKey, alias='type')

```

#### `` in\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKey.in_ "Permanent link")

```
in_ = Field(alias='in')

```

#### `` name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKey.name "Permanent link")

```
name

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKey.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKey.description "Permanent link")

```
description = None

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKey.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.APIKey.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` HTTPBase [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBase "Permanent link")

Bases: `SecurityBase`

#### `` type\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBase.type_ "Permanent link")

```
type_ = Field(default=http, alias='type')

```

#### `` scheme`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBase.scheme "Permanent link")

```
scheme

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBase.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBase.description "Permanent link")

```
description = None

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBase.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBase.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` HTTPBearer [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBearer "Permanent link")

Bases: `HTTPBase`

#### `` scheme`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBearer.scheme "Permanent link")

```
scheme = 'bearer'

```

#### `` bearerFormat`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBearer.bearerFormat "Permanent link")

```
bearerFormat = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBearer.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` type\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBearer.type_ "Permanent link")

```
type_ = Field(default=http, alias='type')

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBearer.description "Permanent link")

```
description = None

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBearer.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.HTTPBearer.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` OAuthFlow [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlow "Permanent link")

Bases: `BaseModelWithConfig`

#### `` refreshUrl`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlow.refreshUrl "Permanent link")

```
refreshUrl = None

```

#### `` scopes`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlow.scopes "Permanent link")

```
scopes = {}

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlow.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlow.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlow.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` OAuthFlowImplicit [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowImplicit "Permanent link")

Bases: `OAuthFlow`

#### `` authorizationUrl`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowImplicit.authorizationUrl "Permanent link")

```
authorizationUrl

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowImplicit.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` refreshUrl`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowImplicit.refreshUrl "Permanent link")

```
refreshUrl = None

```

#### `` scopes`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowImplicit.scopes "Permanent link")

```
scopes = {}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowImplicit.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowImplicit.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` OAuthFlowPassword [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowPassword "Permanent link")

Bases: `OAuthFlow`

#### `` tokenUrl`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowPassword.tokenUrl "Permanent link")

```
tokenUrl

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowPassword.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` refreshUrl`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowPassword.refreshUrl "Permanent link")

```
refreshUrl = None

```

#### `` scopes`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowPassword.scopes "Permanent link")

```
scopes = {}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowPassword.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowPassword.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` OAuthFlowClientCredentials [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowClientCredentials "Permanent link")

Bases: `OAuthFlow`

#### `` tokenUrl`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowClientCredentials.tokenUrl "Permanent link")

```
tokenUrl

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowClientCredentials.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` refreshUrl`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowClientCredentials.refreshUrl "Permanent link")

```
refreshUrl = None

```

#### `` scopes`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowClientCredentials.scopes "Permanent link")

```
scopes = {}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowClientCredentials.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowClientCredentials.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` OAuthFlowAuthorizationCode [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowAuthorizationCode "Permanent link")

Bases: `OAuthFlow`

#### `` authorizationUrl`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowAuthorizationCode.authorizationUrl "Permanent link")

```
authorizationUrl

```

#### `` tokenUrl`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowAuthorizationCode.tokenUrl "Permanent link")

```
tokenUrl

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowAuthorizationCode.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` refreshUrl`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowAuthorizationCode.refreshUrl "Permanent link")

```
refreshUrl = None

```

#### `` scopes`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowAuthorizationCode.scopes "Permanent link")

```
scopes = {}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowAuthorizationCode.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlowAuthorizationCode.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` OAuthFlows [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlows "Permanent link")

Bases: `BaseModelWithConfig`

#### `` implicit`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlows.implicit "Permanent link")

```
implicit = None

```

#### `` password`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlows.password "Permanent link")

```
password = None

```

#### `` clientCredentials`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlows.clientCredentials "Permanent link")

```
clientCredentials = None

```

#### `` authorizationCode`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlows.authorizationCode "Permanent link")

```
authorizationCode = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlows.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlows.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuthFlows.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` OAuth2 [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuth2 "Permanent link")

Bases: `SecurityBase`

#### `` type\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuth2.type_ "Permanent link")

```
type_ = Field(default=oauth2, alias='type')

```

#### `` flows`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuth2.flows "Permanent link")

```
flows

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuth2.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuth2.description "Permanent link")

```
description = None

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuth2.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OAuth2.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` OpenIdConnect [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenIdConnect "Permanent link")

Bases: `SecurityBase`

#### `` type\_`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenIdConnect.type_ "Permanent link")

```
type_ = Field(default=openIdConnect, alias='type')

```

#### `` openIdConnectUrl`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenIdConnect.openIdConnectUrl "Permanent link")

```
openIdConnectUrl

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenIdConnect.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenIdConnect.description "Permanent link")

```
description = None

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenIdConnect.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenIdConnect.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Components [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components "Permanent link")

Bases: `BaseModelWithConfig`

#### `` schemas`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.schemas "Permanent link")

```
schemas = None

```

#### `` responses`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.responses "Permanent link")

```
responses = None

```

#### `` parameters`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.parameters "Permanent link")

```
parameters = None

```

#### `` examples`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.examples "Permanent link")

```
examples = None

```

#### `` requestBodies`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.requestBodies "Permanent link")

```
requestBodies = None

```

#### `` headers`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.headers "Permanent link")

```
headers = None

```

#### `` securitySchemes`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.securitySchemes "Permanent link")

```
securitySchemes = None

```

#### `` links`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.links "Permanent link")

```
links = None

```

#### `` callbacks`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.callbacks "Permanent link")

```
callbacks = None

```

#### `` pathItems`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.pathItems "Permanent link")

```
pathItems = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Components.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` Tag [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Tag "Permanent link")

Bases: `BaseModelWithConfig`

#### `` name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Tag.name "Permanent link")

```
name

```

#### `` description`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Tag.description "Permanent link")

```
description = None

```

#### `` externalDocs`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Tag.externalDocs "Permanent link")

```
externalDocs = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Tag.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Tag.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.Tag.Config.extra "Permanent link")

```
extra = 'allow'

```

### `` OpenAPI [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI "Permanent link")

Bases: `BaseModelWithConfig`

#### `` openapi`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.openapi "Permanent link")

```
openapi

```

#### `` info`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.info "Permanent link")

```
info

```

#### `` jsonSchemaDialect`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.jsonSchemaDialect "Permanent link")

```
jsonSchemaDialect = None

```

#### `` servers`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.servers "Permanent link")

```
servers = None

```

#### `` paths`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.paths "Permanent link")

```
paths = None

```

#### `` webhooks`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.webhooks "Permanent link")

```
webhooks = None

```

#### `` components`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.components "Permanent link")

```
components = None

```

#### `` security`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.security "Permanent link")

```
security = None

```

#### `` tags`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.tags "Permanent link")

```
tags = None

```

#### `` externalDocs`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.externalDocs "Permanent link")

```
externalDocs = None

```

#### `` model\_config`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.model_config "Permanent link")

```
model_config = {'extra': 'allow'}

```

#### `` Config [¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.Config "Permanent link")

##### `` extra`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/openapi/models/\#fastapi.openapi.models.OpenAPI.Config.extra "Permanent link")

```
extra = 'allow'

```