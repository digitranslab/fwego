# Application type

An application is an abstraction that a user can add to workspace. More information about 
this can be found in the [introduction](../technical/introduction.md). This is a
tutorial about how you can add your own application to Fwego via a plugin. We are 
going to create a text file application. In the end a user can use the "Create new" 
button to create a text file and add it to a workspace. We expect that you are using the
[plugin boilerplate](./boilerplate.md).

## Backend

We are going to start by creating a new application type instance for our text file and
add it to the application type registry. By doing this the Fwego backend knows we 
have an additional application type names `text_file`. Creating the following python 
classes and modify the plugins config. Every time a user creates a new text file 
application a TextFile model instance is automatically created. It is also possible to 
save unique attributes for each created text file by adding the properties to the 
model, but we do not need that in this case.

plugins/my_fwego_plugin/backend/src/my_fwego_plugin/models.py
```python
from fwego.core.models import Application

class TextFile(Application):
    pass
```

plugins/my_fwego_plugin/backend/src/my_fwego_plugin/application_types.py
```python
from fwego.core.registries import ApplicationType

from .models import TextFile


class TextFileApplicationType(ApplicationType):
    type = 'text_file'
    model_class = TextFile
```

plugins/my_fwego_plugin/backend/src/my_fwego_plugin/config.py
```python
from django.apps import AppConfig

from fwego.core.registries import plugin_registry, application_type_registry


class PluginNameConfig(AppConfig):
    name = 'my_fwego_plugin'

    def ready(self):
        from .plugins import PluginNamePlugin
        from .application_types import TextFileApplicationType

        plugin_registry.register(PluginNamePlugin())
        application_type_registry.register(TextFileApplicationType())
```

Once these files have been created you first need to apply the schema changes because 
we need the table related to the TextFile model. Execute the following commands inside 
the backend container.

```
$ fwego makemigrations my_fwego_plugin
$ fwego migrate 
```

Lets try to create a new application with the `text_file` type by calling the 
`create_application` endpoint. More information on how to do this can be found in the
[api docs](../apis/rest-api.md) and in the 
[create application api spec](https://api.fwego.io/api/redoc/#operation/create_application).
If that succeeds you are ready to get to the next web-frontend part. You might want to 
inspect the `backend/src/fwego/core/registries.py::ApplicationType` class for all the
options.

## Web frontend

Because the backend and web-frontend are two separate applications that only 
communicate via a REST API with each other, the web-frontend does not yet know about 
the existence of the `text_file` application type. We can add this in a similar way.
Add/modify the following files in the web-frontend part of the plugin.

plugins/my_fwego_plugin/web-frontend/applicationTypes.js
```javascript
import { ApplicationType } from '@fwego/modules/core/applicationTypes'

export class TextFileApplicationType extends ApplicationType {
  static getType() {
    return 'text_file'
  }

  getIconClass() {
    return 'iconoir-file-alt'
  }

  getName() {
    return 'Text file'
  }

  select(application) {
    console.log(`text file selected with id from dashboard ${application.id}`)
  }
}
```

plugins/my_fwego_plugin/web-frontend/plugin.js
```javascript
import { PluginNamePlugin } from '@my-fwego-plugin/plugins'
import { TextFileApplicationType } from '@my-fwego-plugin/applicationTypes'

export default (context) => {
  const { app } = context
  app.$registry.register('plugin', new PluginNamePlugin(context))
  app.$registry.register('application', new TextFileApplicationType(context))
}
```

Once you have added this code you should be able to use the "Create new" button in the
sidebar of the web-frontend to create a new text file. Of course if you click on it in 
the state right now it does not do anything. There are several methods that can 
be overridden in the `TextFileApplicationType` class. You can for example create a new 
route and provide that route name in the `getRouteName` method if you want to navigate 
to that route when the user clicks on the text file in the sidebar. You might want to 
inspect the `web-frontend/modules/core/applicationTypes.js` file in the Fwego 
repository for all the options.
