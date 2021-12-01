import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="fast_basic",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="fast_basic_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from fast_basic.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export fast_basic_KEY=value
export fast_basic_KEY="@int 42"
export fast_basic_KEY="@jinja {{ this.db.uri }}"
export fast_basic_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
fast_basic_ENV=production fast_basic run
```

Read more on https://dynaconf.com
"""
