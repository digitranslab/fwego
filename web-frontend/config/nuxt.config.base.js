export default function (
  base = '@',
  premiumBase = '@/../premium/web-frontend',
  enterpriseBase = '@/../enterprise/web-frontend'
) {
  // Support adding in extra modules say from a plugin using the ADDITIONAL_MODULES
  // env variable which is a comma separated list of absolute module paths.
  const additionalModulesCsv = process.env.ADDITIONAL_MODULES
  const additionalModules = additionalModulesCsv
    ? additionalModulesCsv
        .split(',')
        .map((m) => m.trim())
        .filter((m) => m !== '')
    : []

  if (additionalModules.length > 0) {
    console.log(`Loading extra plugin modules: ${additionalModules}`)
  }
  const baseModules = [
    base + '/modules/core/module.js',
    base + '/modules/database/module.js',
    base + '/modules/integrations/module.js',
    base + '/modules/builder/module.js',
    base + '/modules/dashboard/module.js',
  ]
  if (!process.env.FWEGO_OSS_ONLY) {
    baseModules.push(
      premiumBase + '/modules/fwego_premium/module.js',
      enterpriseBase + '/modules/fwego_enterprise/module.js'
    )
  }
  baseModules.push('@nuxtjs/sentry')

  const modules = baseModules.concat(additionalModules)
  return {
    modules,
    buildModules: ['@nuxtjs/stylelint-module', '@nuxtjs/svg'],
    sentry: {
      clientIntegrations: {
        Dedupe: {},
        ExtraErrorData: {},
        RewriteFrames: {},
        ReportingObserver: null,
      },
      clientConfig: {
        attachProps: true,
        logErrors: true,
      },
    },
    build: {
      extend(config, ctx) {
        config.node = { fs: 'empty' }
        config.module.rules.push({
          test: /\.(m|c)js$/,
          include: /node_modules/,
          type: 'javascript/auto',
        })
      },
      babel: { compact: true },
      transpile: ['axios', 'tiptap-markdown', 'markdown-it'],
    },
  }
}