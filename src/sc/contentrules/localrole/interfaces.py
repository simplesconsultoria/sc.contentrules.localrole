# -*- coding: utf-8 -*-
from zope.interface import Interface

from zope.schema import Choice
from zope.schema import Set
from zope.schema import TextLine

from sc.contentrules.localrole import MessageFactory as _


class ILocalRoleAction(Interface):
    """An action used to apply a local role to an object
    """

    principal = TextLine(title=_(u"Username / Group name"),
                         description=_(u"Please inform the username or "
                                       u"groupname that will be used by "
                                       u"this action."),
                         required=True)

    roles = Set(title=_(u"Roles"),
                description=_(u"Roles to be assigned to user/group "
                              u"in the object."),
                required=True,
                value_type=Choice(vocabulary='plone.app.vocabularies.Roles')
                )
