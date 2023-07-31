# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "palo-alto cloudngfw firewall show-log-profile",
)
class ShowLogProfile(AAZCommand):
    """Get Log Profile for Firewall

    :example: Get Log Profile for Firewall
        az palo-alto cloudngfw firewall show-log-profile --resource-group MyResourceGroup -n MyCloudngfwFirewall
    """

    _aaz_info = {
        "version": "2022-08-29",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/paloaltonetworks.cloudngfw/firewalls/{}/getlogprofile", "2022-08-29"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.firewall_name = AAZStrArg(
            options=["-n", "--name", "--firewall-name"],
            help="Firewall resource name",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.FirewallsGetLogProfile(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class FirewallsGetLogProfile(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/PaloAltoNetworks.Cloudngfw/firewalls/{firewallName}/getLogProfile",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "firewallName", self.ctx.args.firewall_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-08-29",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.application_insights = AAZObjectType(
                serialized_name="applicationInsights",
            )
            _schema_on_200.common_destination = AAZObjectType(
                serialized_name="commonDestination",
            )
            _ShowLogProfileHelper._build_schema_log_destination_read(_schema_on_200.common_destination)
            _schema_on_200.decrypt_log_destination = AAZObjectType(
                serialized_name="decryptLogDestination",
            )
            _ShowLogProfileHelper._build_schema_log_destination_read(_schema_on_200.decrypt_log_destination)
            _schema_on_200.log_option = AAZStrType(
                serialized_name="logOption",
            )
            _schema_on_200.log_type = AAZStrType(
                serialized_name="logType",
            )
            _schema_on_200.threat_log_destination = AAZObjectType(
                serialized_name="threatLogDestination",
            )
            _ShowLogProfileHelper._build_schema_log_destination_read(_schema_on_200.threat_log_destination)
            _schema_on_200.traffic_log_destination = AAZObjectType(
                serialized_name="trafficLogDestination",
            )
            _ShowLogProfileHelper._build_schema_log_destination_read(_schema_on_200.traffic_log_destination)

            application_insights = cls._schema_on_200.application_insights
            application_insights.id = AAZStrType()
            application_insights.key = AAZStrType()

            return cls._schema_on_200


class _ShowLogProfileHelper:
    """Helper class for ShowLogProfile"""

    _schema_log_destination_read = None

    @classmethod
    def _build_schema_log_destination_read(cls, _schema):
        if cls._schema_log_destination_read is not None:
            _schema.event_hub_configurations = cls._schema_log_destination_read.event_hub_configurations
            _schema.monitor_configurations = cls._schema_log_destination_read.monitor_configurations
            _schema.storage_configurations = cls._schema_log_destination_read.storage_configurations
            return

        cls._schema_log_destination_read = _schema_log_destination_read = AAZObjectType()

        log_destination_read = _schema_log_destination_read
        log_destination_read.event_hub_configurations = AAZObjectType(
            serialized_name="eventHubConfigurations",
        )
        log_destination_read.monitor_configurations = AAZObjectType(
            serialized_name="monitorConfigurations",
        )
        log_destination_read.storage_configurations = AAZObjectType(
            serialized_name="storageConfigurations",
        )

        event_hub_configurations = _schema_log_destination_read.event_hub_configurations
        event_hub_configurations.id = AAZStrType()
        event_hub_configurations.name = AAZStrType()
        event_hub_configurations.name_space = AAZStrType(
            serialized_name="nameSpace",
        )
        event_hub_configurations.policy_name = AAZStrType(
            serialized_name="policyName",
        )
        event_hub_configurations.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
        )

        monitor_configurations = _schema_log_destination_read.monitor_configurations
        monitor_configurations.id = AAZStrType()
        monitor_configurations.primary_key = AAZStrType(
            serialized_name="primaryKey",
        )
        monitor_configurations.secondary_key = AAZStrType(
            serialized_name="secondaryKey",
        )
        monitor_configurations.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
        )
        monitor_configurations.workspace = AAZStrType()

        storage_configurations = _schema_log_destination_read.storage_configurations
        storage_configurations.account_name = AAZStrType(
            serialized_name="accountName",
        )
        storage_configurations.id = AAZStrType()
        storage_configurations.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
        )

        _schema.event_hub_configurations = cls._schema_log_destination_read.event_hub_configurations
        _schema.monitor_configurations = cls._schema_log_destination_read.monitor_configurations
        _schema.storage_configurations = cls._schema_log_destination_read.storage_configurations


__all__ = ["ShowLogProfile"]