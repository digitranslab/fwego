# Install on Railway

Railway is a cloud platform that allows you to instantly deploy and scale applications.
They have over 200 templates that can easily be deployed, and Fwego is one of them.

## Create an account

If you don't have an account already, you can navigate to https://railway.app/, and
create a new account.

## Start new project

After that you can click on the button `Start a New Project`, search for `Fwego`,
click on it, and you will immediately see the preconfigured settings. Click on the
`Deploy` button, and wait until all the services spin up.

## Launch

When the containers started, you can click on the Fwego one, and then click on the
`***.railway.app` link to open Fwego.

## Not compatible with Trial plan

Fwego is unfortunately not compatible with the trial plan. It has a maximum of 512 MB
of memory, and even running Fwego with environment variable `FWEGO_RUN_MINIMAL=True`
it's not enough to run the all-in-one image. You have to be on the Hobby plan at
minimal.
