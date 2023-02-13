from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import plone_mountain_site


class PLONE_MOUNTAIN_SITELayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plone_mountain_site)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plone_mountain_site:default")
        applyProfile(portal, "plone_mountain_site:initial")


PLONE_MOUNTAIN_SITE_FIXTURE = PLONE_MOUNTAIN_SITELayer()


PLONE_MOUNTAIN_SITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_MOUNTAIN_SITE_FIXTURE,),
    name="PLONE_MOUNTAIN_SITELayer:IntegrationTesting",
)


PLONE_MOUNTAIN_SITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_MOUNTAIN_SITE_FIXTURE, WSGI_SERVER_FIXTURE),
    name="PLONE_MOUNTAIN_SITELayer:FunctionalTesting",
)


PLONE_MOUNTAIN_SITEACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONE_MOUNTAIN_SITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="PLONE_MOUNTAIN_SITELayer:AcceptanceTesting",
)
