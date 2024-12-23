# Introduction

Fwego plugins let you fully customize and extend Fwego quickly and easily. Multiple
plugins can be installed into a new or existing Fwego installation, they get full
access to Fwego's internals for maximum customization and are straightforward develop
and publish.

Some examples of what you can do with a Fwego plugin are:

* Add new Fwego:
    * Field Types
    * View Types/Filters/Sorts/Decorations/Aggregations
    * Formula Functions/Types
* Add or customize pages, components, styling
* Integrate with 3rd party APIs or software
* Install custom postgres extensions, system packages, python and node dependencies
* And much more!

Fwego Plugins are only available for self-hosted installations currently and are 
**experimental** and subject to change.

1. **You should always make backups of your Fwego data before installing and using any
   plugin.**
2. **You should only ever install plugins from a trusted source.**
3. **Fwego is not responsible for and does not officially support any plugins
   currently, installing and using them is entirely at your own risk.**

## Installing a Plugin

The [Plugin Installation](./installation.md) guide goes into detail on how to install
and uninstall Fwego plugins in the various official Fwego docker images.

Currently, we do not provide an officially supported plugins, however check out our
[Plugin community sub-forum](https://community.fwego.io/c/plugins/17) for community
made plugins and further discussion.

## Step by step plugin creation tutorial

Check out
our [step by step tutorial on plugin creation using the plugin boilerplate](./boilerplate.md)
for a quick and easy way to get a plugin started.

## Creating a Plugin

Finally, the [Plugin Creation](./creation.md) guide explains in more detail how to
create your own plugins and publish them for others to use.

