# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from io import IOBase
import json
from typing import Any, AsyncIterator, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ...operations._operations import (
    build_hsm_security_domain_download_pending_request,
    build_hsm_security_domain_download_request,
    build_hsm_security_domain_transfer_key_request,
    build_hsm_security_domain_upload_pending_request,
    build_hsm_security_domain_upload_request,
)

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class HsmSecurityDomainOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.keyvault.securitydomain.aio.KeyVaultClient`'s
        :attr:`hsm_security_domain` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def download_pending(self, **kwargs: Any) -> _models.SecurityDomainOperationStatus:
        """Retrieves the Security Domain download operation status.

        :return: SecurityDomainOperationStatus. The SecurityDomainOperationStatus is compatible with
         MutableMapping
        :rtype: ~azure.keyvault.securitydomain.models.SecurityDomainOperationStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.SecurityDomainOperationStatus] = kwargs.pop("cls", None)

        _request = build_hsm_security_domain_download_pending_request(
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url(
                "self._config.vault_base_url", self._config.vault_base_url, "str", skip_quote=True
            ),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.SecurityDomainOperationStatus, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _download_initial(
        self, certificate_info_object: Union[_models.CertificateInfoObject, JSON, IO[bytes]], **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(certificate_info_object, (IOBase, bytes)):
            _content = certificate_info_object
        else:
            _content = json.dumps(certificate_info_object, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_hsm_security_domain_download_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url(
                "self._config.vault_base_url", self._config.vault_base_url, "str", skip_quote=True
            ),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Azure-AsyncOperation"] = self._deserialize(
            "str", response.headers.get("Azure-AsyncOperation")
        )
        response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_download(
        self,
        certificate_info_object: _models.CertificateInfoObject,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SecurityDomainOperationStatus]:
        """Retrieves the Security Domain from the managed HSM. Calling this endpoint can
        be used to activate a provisioned managed HSM resource.

        :param certificate_info_object: The Security Domain download operation requires customer to
         provide N certificates (minimum 3 and maximum 10)
         containing a public key in JWK format. Required.
        :type certificate_info_object: ~azure.keyvault.securitydomain.models.CertificateInfoObject
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns SecurityDomainOperationStatus. The
         SecurityDomainOperationStatus is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.keyvault.securitydomain.models.SecurityDomainOperationStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_download(
        self, certificate_info_object: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.SecurityDomainOperationStatus]:
        """Retrieves the Security Domain from the managed HSM. Calling this endpoint can
        be used to activate a provisioned managed HSM resource.

        :param certificate_info_object: The Security Domain download operation requires customer to
         provide N certificates (minimum 3 and maximum 10)
         containing a public key in JWK format. Required.
        :type certificate_info_object: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns SecurityDomainOperationStatus. The
         SecurityDomainOperationStatus is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.keyvault.securitydomain.models.SecurityDomainOperationStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_download(
        self, certificate_info_object: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.SecurityDomainOperationStatus]:
        """Retrieves the Security Domain from the managed HSM. Calling this endpoint can
        be used to activate a provisioned managed HSM resource.

        :param certificate_info_object: The Security Domain download operation requires customer to
         provide N certificates (minimum 3 and maximum 10)
         containing a public key in JWK format. Required.
        :type certificate_info_object: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns SecurityDomainOperationStatus. The
         SecurityDomainOperationStatus is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.keyvault.securitydomain.models.SecurityDomainOperationStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_download(
        self, certificate_info_object: Union[_models.CertificateInfoObject, JSON, IO[bytes]], **kwargs: Any
    ) -> AsyncLROPoller[_models.SecurityDomainOperationStatus]:
        """Retrieves the Security Domain from the managed HSM. Calling this endpoint can
        be used to activate a provisioned managed HSM resource.

        :param certificate_info_object: The Security Domain download operation requires customer to
         provide N certificates (minimum 3 and maximum 10)
         containing a public key in JWK format. Is one of the following types: CertificateInfoObject,
         JSON, IO[bytes] Required.
        :type certificate_info_object: ~azure.keyvault.securitydomain.models.CertificateInfoObject or
         JSON or IO[bytes]
        :return: An instance of AsyncLROPoller that returns SecurityDomainOperationStatus. The
         SecurityDomainOperationStatus is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.keyvault.securitydomain.models.SecurityDomainOperationStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SecurityDomainOperationStatus] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._download_initial(
                certificate_info_object=certificate_info_object,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

            deserialized = _deserialize(_models.SecurityDomainOperationStatus, response.json())
            if cls:
                return cls(pipeline_response, deserialized, response_headers)  # type: ignore
            return deserialized

        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url(
                "self._config.vault_base_url", self._config.vault_base_url, "str", skip_quote=True
            ),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.SecurityDomainOperationStatus].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.SecurityDomainOperationStatus](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @distributed_trace_async
    async def transfer_key(self, **kwargs: Any) -> _models.TransferKey:
        """Retrieve Security Domain transfer key.

        :return: TransferKey. The TransferKey is compatible with MutableMapping
        :rtype: ~azure.keyvault.securitydomain.models.TransferKey
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.TransferKey] = kwargs.pop("cls", None)

        _request = build_hsm_security_domain_transfer_key_request(
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url(
                "self._config.vault_base_url", self._config.vault_base_url, "str", skip_quote=True
            ),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.TransferKey, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _upload_initial(
        self, security_domain: Union[_models.SecurityDomainObject, JSON, IO[bytes]], **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(security_domain, (IOBase, bytes)):
            _content = security_domain
        else:
            _content = json.dumps(security_domain, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_hsm_security_domain_upload_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url(
                "self._config.vault_base_url", self._config.vault_base_url, "str", skip_quote=True
            ),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_upload(
        self, security_domain: _models.SecurityDomainObject, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.SecurityDomainOperationStatus]:
        """Restore the provided Security Domain.

        :param security_domain: The Security Domain to be restored. Required.
        :type security_domain: ~azure.keyvault.securitydomain.models.SecurityDomainObject
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns SecurityDomainOperationStatus. The
         SecurityDomainOperationStatus is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.keyvault.securitydomain.models.SecurityDomainOperationStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_upload(
        self, security_domain: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.SecurityDomainOperationStatus]:
        """Restore the provided Security Domain.

        :param security_domain: The Security Domain to be restored. Required.
        :type security_domain: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns SecurityDomainOperationStatus. The
         SecurityDomainOperationStatus is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.keyvault.securitydomain.models.SecurityDomainOperationStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_upload(
        self, security_domain: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.SecurityDomainOperationStatus]:
        """Restore the provided Security Domain.

        :param security_domain: The Security Domain to be restored. Required.
        :type security_domain: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns SecurityDomainOperationStatus. The
         SecurityDomainOperationStatus is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.keyvault.securitydomain.models.SecurityDomainOperationStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_upload(
        self, security_domain: Union[_models.SecurityDomainObject, JSON, IO[bytes]], **kwargs: Any
    ) -> AsyncLROPoller[_models.SecurityDomainOperationStatus]:
        """Restore the provided Security Domain.

        :param security_domain: The Security Domain to be restored. Is one of the following types:
         SecurityDomainObject, JSON, IO[bytes] Required.
        :type security_domain: ~azure.keyvault.securitydomain.models.SecurityDomainObject or JSON or
         IO[bytes]
        :return: An instance of AsyncLROPoller that returns SecurityDomainOperationStatus. The
         SecurityDomainOperationStatus is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.keyvault.securitydomain.models.SecurityDomainOperationStatus]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SecurityDomainOperationStatus] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._upload_initial(
                security_domain=security_domain,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

            deserialized = _deserialize(_models.SecurityDomainOperationStatus, response.json())
            if cls:
                return cls(pipeline_response, deserialized, response_headers)  # type: ignore
            return deserialized

        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url(
                "self._config.vault_base_url", self._config.vault_base_url, "str", skip_quote=True
            ),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.SecurityDomainOperationStatus].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.SecurityDomainOperationStatus](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @distributed_trace_async
    async def upload_pending(self, **kwargs: Any) -> _models.SecurityDomainOperationStatus:
        """Get Security Domain upload operation status.

        :return: SecurityDomainOperationStatus. The SecurityDomainOperationStatus is compatible with
         MutableMapping
        :rtype: ~azure.keyvault.securitydomain.models.SecurityDomainOperationStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.SecurityDomainOperationStatus] = kwargs.pop("cls", None)

        _request = build_hsm_security_domain_upload_pending_request(
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url(
                "self._config.vault_base_url", self._config.vault_base_url, "str", skip_quote=True
            ),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.SecurityDomainOperationStatus, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
