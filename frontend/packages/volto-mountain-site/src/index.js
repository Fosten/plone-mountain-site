const applyConfig = (config) => {
  config.settings = {
    ...config.settings,
    matomoSiteId: '2',
    matomoUrlBase: 'https://stats.lillymountain.com/',
    showPloneLogin: false,
    serverConfig: {
      ...config.settings.serverConfig,
      extractScripts: {
        ...config.settings.serverConfig.extractScripts,
        errorPages: true,
      },
    },
  };
  return config;
};

export default applyConfig;
