# Installation on Render

> Any questions, problems or suggestions with this guide? Ask a question in our
> [community](https://community.fwego.io/) or contribute the change yourself at
> https://github.com/digitranslab/fwego/-/tree/develop/docs .

[Render](https://render.com) is a modern alternative to Heroku, a platform as a service.
Render enables you to build, run and operate applications entirely in the cloud. We have
created a template that allows you to easily install Fwego on the "Standard" paid
plan and the paid Postgres plan provided by Render.

## The template

> Currently, we only support running Fwego on the $25 per month "Standard" Render
> plan additionally with their $7 per month Postgres plan for performance reasons.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/digitranslab/fwego/tree/master)
The button above can be used to install Fwego on [Render](https://render.com) with one
click. You may need to manually enter the `https://github.com/digitranslab/fwego/`
repository URL and choose the branch
`master`.

After installation, you can reach Fwego on the URL provided by Render.

## Built-in Fwego templates disabled by default

In our template because we are only using 1 Fwego worker the initial template sync
will block other background tasks, such as exporting tables. As a result we have by
default disabled the loading of our built-in example templates. You can trigger this
manually by:

1. Login Render and go to your Fwego web-service 
2. Click the "Shell" sidebar link
3. Enter and run the following command `./fwego.sh backend-cmd manage sync_templates`

Every time you upgrade your Render Fwego app you will need to repeat the steps above
the get the latest Fwego templates.

## Persistent S3 file storage

By default, the uploaded files are stored inside the Render service for demo purposes.
This means that everytime your render service restarts, you will lose all your uploaded
files. Your files can optionally be stored inside an S3 bucket. To do so, you need to
add a couple of config vars to the settings. Go to your Fwego web-service in Render
and click on the "Environment" section. Here you need to add the following vars:

* AWS_ACCESS_KEY_ID: The access key for your AWS account.
* AWS_SECRET_ACCESS_KEY: The secret key for your AWS account.
* AWS_STORAGE_BUCKET_NAME: Your Amazon Web Services storage bucket name.
* AWS_S3_REGION_NAME *Optional*: Name of the AWS S3 region to use (eg. eu-west-1)
* AWS_S3_ENDPOINT_URL *Optional*: Custom S3 URL to use when connecting to S3, including
  scheme.
* AWS_S3_CUSTOM_DOMAIN *Optional*: Your custom domain where the files can be downloaded
  from.

### Non AWS S3 providers

It is also possible to use non AWS, S3 providers like for example Digital Ocean. Below
you will find example settings if you want to connect to Digital Ocean Spaces.

* AWS_ACCESS_KEY_ID: The spaces API key.
* AWS_SECRET_ACCESS_KEY: The spaces API secret key.
* AWS_STORAGE_BUCKET_NAME: The name of your space.
* AWS_S3_REGION_NAME: Name of the Digital Ocean spaces region (eg. ams3)
* AWS_S3_ENDPOINT_URL: (eg. https://ams3.digitaloceanspaces.com)
* AWS_S3_CUSTOM_DOMAIN: (eg. name-of-your-space.ams3.digitaloceanspaces.com)

### Workers per service

To spare resources, every Fwego service in Render has only one worker by default. If
you are upgrading to a more powerful Render plan, you can increase the amount of workers
to 2. This can be done via the Environment section on your Fwego web-service in
Render. Find the "FWEGO_AMOUNT_OF_WORKERS" var and set the value to your desired
number of workers.

You can roughly estimate the amount of workers based on the available RAM of your
service type. Every worker needs around 512MB ram.

## Updating to the latest version of Fwego

When a new version of Fwego has been released, you probably want to update. To do so
on your render Fwego web-service you can click the "Manual Deploy" button and select "
Deploy latest commit".
