from flask import  Flask,render_template,session,redirect,url_for
from wtforms import StringField, PasswordField , SubmitField , RadioField,TextAreaField
from flask_wtf import FlaskForm
from  wtforms.validators import  DataRequired,Length,EqualTo, Email
from flask_wtf import FlaskForm
import json_loads
from requests.auth import AuthBase

"""
This module implements a friendly (well, friendlier) interface between the raw JSON
responses from Jira and the Resource/dict abstractions provided by this library. Users
will construct a JIRA object as described below. Full API documentation can be found
at: https://jira.readthedocs.io/en/latest/
"""
from functools import lru_cache
from functools import wraps

import imghdr
import mimetypes

from collections.abc import Iterable
import copy
import json
import logging
import os
import re


import calendar
import datetime
import hashlib
from numbers import Number
import requests
import sys
import time
import warnings

from requests.utils import get_netrc_auth
from urllib.parse import urlparse

# GreenHopper specific resources
from jira.exceptions import JIRAError
from jira.resilientsession import raise_on_error
from jira.resilientsession import ResilientSession

# Jira-specific resources
from jira.resources import Attachment
from jira.resources import Board
from jira.resources import Comment
from jira.resources import Component
from jira.resources import Customer
from jira.resources import CustomFieldOption
from jira.resources import Dashboard
from jira.resources import Filter
from jira.resources import GreenHopperResource
from jira.resources import Issue
from jira.resources import IssueLink
from jira.resources import IssueLinkType
from jira.resources import IssueType
from jira.resources import Priority
from jira.resources import Project
from jira.resources import RemoteLink
from jira.resources import RequestType
from jira.resources import Resolution
from jira.resources import Resource
from jira.resources import Role
from jira.resources import SecurityLevel
from jira.resources import ServiceDesk
from jira.resources import Sprint
from jira.resources import Status
from jira.resources import StatusCategory
from jira.resources import User
from jira.resources import Group
from jira.resources import Version
from jira.resources import Votes
from jira.resources import Watchers
from jira.resources import Worklog

from jira import __version__
from jira.utils import CaseInsensitiveDict
from jira.utils import json_loads
from jira.utils import threaded_requests
from pkg_resources import parse_version

from collections import OrderedDict

try:
    # noinspection PyUnresolvedReferences
    from requests_toolbelt import MultipartEncoder
except ImportError:
    pass

try:
    from requests_jwt import JWTAuth
except ImportError:
    pass


logging.getLogger("jira").addHandler(logging.NullHandler())





class signupForm(FlaskForm):
     email=StringField(label='email',validators=[DataRequired(),Email()])
     password=PasswordField(label='password',validators=[DataRequired(),Length(min=6,max=8)])
     id=StringField(label='id',validators=[DataRequired(),Length(min=9,max=9)])
     firstname=StringField(label='firstname',validators=[DataRequired(),Length(min=3,max=20)])
     lastname=StringField(label='lastname',validators=[DataRequired(),Length(min=3,max=20)])
     submit=SubmitField(label='Sign up')



class LoginForm(FlaskForm):
    email=StringField(label='email',validators=[DataRequired(),Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=6, max=8)])
    submit = SubmitField('Login')

class SignOutForm(FlaskForm):
    submit = SubmitField('logout')

class update_sprint(FlaskForm):
        DEFAULT_OPTIONS = {
        "server": "http://localhost:2990/jira",
        "auth_url": "/rest/auth/1/session",
        "context_path": "/",
        "rest_path": "api",
        "rest_api_version": "2",
        "agile_rest_path": GreenHopperResource.GREENHOPPER_REST_PATH,
        "agile_rest_api_version": "1.0",
        "verify": True,
        "resilient": True,
        "async": False,
        "async_workers": 5,
        "client_cert": None,
        "check_update": False,
        # amount of seconds to wait for loading a resource after updating it
        # used to avoid server side caching issues, used to be 4 seconds.
        "delay_reload": 0,
        "headers": {
            "Cache-Control": "no-cache",
            # 'Accept': 'application/json;charset=UTF-8',  # default for REST
            "Content-Type": "application/json",  # ;charset=UTF-8',
            # 'Accept': 'application/json',  # default for REST
            # 'Pragma': 'no-cache',
            # 'Expires': 'Thu, 01 Jan 1970 00:00:00 GMT'
            "X-Atlassian-Token": "no-check",
        }
    }

    checked_version = False

    # TODO(ssbarnea): remove these two variables and use the ones defined in resources
    JIRA_BASE_URL = Resource.JIRA_BASE_URL
    AGILE_BASE_URL = GreenHopperResource.AGILE_BASE_URL
      self.sys_version_info = tuple([i for i in sys.version_info])

        if options is None:
            options = {}
            if server and hasattr(server, "keys"):
                warnings.warn(
                    "Old API usage, use JIRA(url) or JIRA(options={'server': url}, when using dictionary always use named parameters.",
                    DeprecationWarning,
                )
                options = server
                server = None

        if server:
            options["server"] = server
        if async_:
            options["async"] = async_
            options["async_workers"] = async_workers

        self.logging = logging

        self._options = copy.copy(JIRA.DEFAULT_OPTIONS)

        self._options.update(options)

        self._rank = None

        # Rip off trailing slash since all urls depend on that
        if self._options["server"].endswith("/"):
            self._options["server"] = self._options["server"][:-1]

        context_path = urlparse(self.server_url).path
        if len(context_path) > 0:
            self._options["context_path"] = context_path

        self._try_magic()

        if oauth:
            self._create_oauth_session(oauth, timeout)
        elif basic_auth:
            self._create_http_basic_session(*basic_auth, timeout=timeout)
            self._session.headers.update(self._options["headers"])
        elif jwt:
            self._create_jwt_session(jwt, timeout)
        elif kerberos:
            self._create_kerberos_session(timeout, kerberos_options=kerberos_options)
        elif auth:
            self._create_cookie_auth(auth, timeout)
            # always log in for cookie based auth, as we need a first request to be logged in
            validate = True
        else:
            verify = self._options["verify"]
            self._session = ResilientSession(timeout=timeout)
            self._session.verify = verify
        self._session.headers.update(self._options["headers"])

        if "cookies" in self._options:
            self._session.cookies.update(self._options["cookies"])

        self._session.max_retries = max_retries

        if proxies:
            self._session.proxies = proxies

        self.auth = auth
        if validate:
            # This will raise an Exception if you are not allowed to login.
            # It's better to fail faster than later.
            user = self.session()
            if user.raw is None:
                auth_method = (
                    oauth or basic_auth or jwt or kerberos or auth or "anonymous"
                )
                raise JIRAError("Can not log in with %s" % str(auth_method))

        self.deploymentType = None
        if get_server_info:
            # We need version in order to know what API calls are available or not
            si = self.server_info()
            try:
                self._version = tuple(si["versionNumbers"])
            except Exception as e:
                logging.error("invalid server_info: %s", si)
                raise e
            self.deploymentType = si.get("deploymentType")
        else:
            self._version = (0, 0, 0)

        if self._options["check_update"] and not JIRA.checked_version:
            self._check_update_()
            JIRA.checked_version = True

        self._fields = {}
        for f in self.fields():
            if "clauseNames" in f:
                for name in f["clauseNames"]:
                    self._fields[name] = f["id"]

    def update_sprint(self, id, name=None, startDate=None, endDate=None, state=None):
        payload = {}
        if name:
            payload["name"] = name
        if startDate:
            payload["startDate"] = startDate
        if endDate:
            payload["endDate"] = endDate
        if state:
            if (
                self._options["agile_rest_path"]
                == GreenHopperResource.GREENHOPPER_REST_PATH
            ):
                raise NotImplementedError(
                    "Public Jira API does not support state update"
                )
            payload["state"] = state

        url = self._get_url("sprint/%s" % id, base=self.AGILE_BASE_URL)
        r = self._session.put(url, data=json.db(payload))

    return json_loads(r)