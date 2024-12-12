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
    "image list",
)
class List(AAZCommand):
    """List the list of images under a resource group.
    """

    _aaz_info = {
        "version": "2024-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.compute/images", "2024-07-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/images", "2024-07-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        condition_1 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        if condition_0:
            self.ImagesList(ctx=self.ctx)()
        if condition_1:
            self.ImagesListByResourceGroup(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ImagesList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/images",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
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
                    "api-version", "2024-07-01",
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200.value.Element.extended_location
            extended_location.name = AAZStrType()
            extended_location.type = AAZStrType()

            properties = cls._schema_on_200.value.Element.properties
            properties.hyper_v_generation = AAZStrType(
                serialized_name="hyperVGeneration",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.source_virtual_machine = AAZObjectType(
                serialized_name="sourceVirtualMachine",
            )
            _ListHelper._build_schema_sub_resource_read(properties.source_virtual_machine)
            properties.storage_profile = AAZObjectType(
                serialized_name="storageProfile",
            )

            storage_profile = cls._schema_on_200.value.Element.properties.storage_profile
            storage_profile.data_disks = AAZListType(
                serialized_name="dataDisks",
            )
            storage_profile.os_disk = AAZObjectType(
                serialized_name="osDisk",
            )
            storage_profile.zone_resilient = AAZBoolType(
                serialized_name="zoneResilient",
            )

            data_disks = cls._schema_on_200.value.Element.properties.storage_profile.data_disks
            data_disks.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.storage_profile.data_disks.Element
            _element.blob_uri = AAZStrType(
                serialized_name="blobUri",
            )
            _element.caching = AAZStrType()
            _element.disk_encryption_set = AAZObjectType(
                serialized_name="diskEncryptionSet",
            )
            _ListHelper._build_schema_disk_encryption_set_parameters_read(_element.disk_encryption_set)
            _element.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            _element.lun = AAZIntType(
                flags={"required": True},
            )
            _element.managed_disk = AAZObjectType(
                serialized_name="managedDisk",
            )
            _ListHelper._build_schema_sub_resource_read(_element.managed_disk)
            _element.snapshot = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(_element.snapshot)
            _element.storage_account_type = AAZStrType(
                serialized_name="storageAccountType",
            )

            os_disk = cls._schema_on_200.value.Element.properties.storage_profile.os_disk
            os_disk.blob_uri = AAZStrType(
                serialized_name="blobUri",
            )
            os_disk.caching = AAZStrType()
            os_disk.disk_encryption_set = AAZObjectType(
                serialized_name="diskEncryptionSet",
            )
            _ListHelper._build_schema_disk_encryption_set_parameters_read(os_disk.disk_encryption_set)
            os_disk.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            os_disk.managed_disk = AAZObjectType(
                serialized_name="managedDisk",
            )
            _ListHelper._build_schema_sub_resource_read(os_disk.managed_disk)
            os_disk.os_state = AAZStrType(
                serialized_name="osState",
                flags={"required": True},
            )
            os_disk.os_type = AAZStrType(
                serialized_name="osType",
                flags={"required": True},
            )
            os_disk.snapshot = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(os_disk.snapshot)
            os_disk.storage_account_type = AAZStrType(
                serialized_name="storageAccountType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class ImagesListByResourceGroup(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
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
                    "api-version", "2024-07-01",
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200.value.Element.extended_location
            extended_location.name = AAZStrType()
            extended_location.type = AAZStrType()

            properties = cls._schema_on_200.value.Element.properties
            properties.hyper_v_generation = AAZStrType(
                serialized_name="hyperVGeneration",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.source_virtual_machine = AAZObjectType(
                serialized_name="sourceVirtualMachine",
            )
            _ListHelper._build_schema_sub_resource_read(properties.source_virtual_machine)
            properties.storage_profile = AAZObjectType(
                serialized_name="storageProfile",
            )

            storage_profile = cls._schema_on_200.value.Element.properties.storage_profile
            storage_profile.data_disks = AAZListType(
                serialized_name="dataDisks",
            )
            storage_profile.os_disk = AAZObjectType(
                serialized_name="osDisk",
            )
            storage_profile.zone_resilient = AAZBoolType(
                serialized_name="zoneResilient",
            )

            data_disks = cls._schema_on_200.value.Element.properties.storage_profile.data_disks
            data_disks.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.storage_profile.data_disks.Element
            _element.blob_uri = AAZStrType(
                serialized_name="blobUri",
            )
            _element.caching = AAZStrType()
            _element.disk_encryption_set = AAZObjectType(
                serialized_name="diskEncryptionSet",
            )
            _ListHelper._build_schema_disk_encryption_set_parameters_read(_element.disk_encryption_set)
            _element.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            _element.lun = AAZIntType(
                flags={"required": True},
            )
            _element.managed_disk = AAZObjectType(
                serialized_name="managedDisk",
            )
            _ListHelper._build_schema_sub_resource_read(_element.managed_disk)
            _element.snapshot = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(_element.snapshot)
            _element.storage_account_type = AAZStrType(
                serialized_name="storageAccountType",
            )

            os_disk = cls._schema_on_200.value.Element.properties.storage_profile.os_disk
            os_disk.blob_uri = AAZStrType(
                serialized_name="blobUri",
            )
            os_disk.caching = AAZStrType()
            os_disk.disk_encryption_set = AAZObjectType(
                serialized_name="diskEncryptionSet",
            )
            _ListHelper._build_schema_disk_encryption_set_parameters_read(os_disk.disk_encryption_set)
            os_disk.disk_size_gb = AAZIntType(
                serialized_name="diskSizeGB",
            )
            os_disk.managed_disk = AAZObjectType(
                serialized_name="managedDisk",
            )
            _ListHelper._build_schema_sub_resource_read(os_disk.managed_disk)
            os_disk.os_state = AAZStrType(
                serialized_name="osState",
                flags={"required": True},
            )
            os_disk.os_type = AAZStrType(
                serialized_name="osType",
                flags={"required": True},
            )
            os_disk.snapshot = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(os_disk.snapshot)
            os_disk.storage_account_type = AAZStrType(
                serialized_name="storageAccountType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_disk_encryption_set_parameters_read = None

    @classmethod
    def _build_schema_disk_encryption_set_parameters_read(cls, _schema):
        if cls._schema_disk_encryption_set_parameters_read is not None:
            _schema.id = cls._schema_disk_encryption_set_parameters_read.id
            return

        cls._schema_disk_encryption_set_parameters_read = _schema_disk_encryption_set_parameters_read = AAZObjectType()

        disk_encryption_set_parameters_read = _schema_disk_encryption_set_parameters_read
        disk_encryption_set_parameters_read.id = AAZStrType()

        _schema.id = cls._schema_disk_encryption_set_parameters_read.id

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["List"]
