# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api_v3/query_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from opentelemetry.proto.trace.v1 import trace_pb2 as opentelemetry_dot_proto_dot_trace_dot_v1_dot_trace__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api_v3/query_service.proto',
  package='jaeger.api_v3',
  syntax='proto3',
  serialized_options=b'\n\027io.jaegertracing.api_v3Z\006api_v3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x61pi_v3/query_service.proto\x12\rjaeger.api_v3\x1a(opentelemetry/proto/trace/v1/trace.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\x81\x01\n\x0fGetTraceRequest\x12\x10\n\x08trace_id\x18\x01 \x01(\t\x12.\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"Y\n\x12SpansResponseChunk\x12\x43\n\x0eresource_spans\x18\x01 \x03(\x0b\x32+.opentelemetry.proto.trace.v1.ResourceSpans\"\x9e\x03\n\x14TraceQueryParameters\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x16\n\x0eoperation_name\x18\x02 \x01(\t\x12G\n\nattributes\x18\x03 \x03(\x0b\x32\x33.jaeger.api_v3.TraceQueryParameters.AttributesEntry\x12\x32\n\x0estart_time_min\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0estart_time_max\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0c\x64uration_min\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0c\x64uration_max\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x12\n\nnum_traces\x18\x08 \x01(\x05\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"G\n\x11\x46indTracesRequest\x12\x32\n\x05query\x18\x01 \x01(\x0b\x32#.jaeger.api_v3.TraceQueryParameters\"\x14\n\x12GetServicesRequest\"\'\n\x13GetServicesResponse\x12\x10\n\x08services\x18\x01 \x03(\t\":\n\x14GetOperationsRequest\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x11\n\tspan_kind\x18\x02 \x01(\t\",\n\tOperation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tspan_kind\x18\x02 \x01(\t\"E\n\x15GetOperationsResponse\x12,\n\noperations\x18\x01 \x03(\x0b\x32\x18.jaeger.api_v3.Operation2\xee\x02\n\x0cQueryService\x12Q\n\x08GetTrace\x12\x1e.jaeger.api_v3.GetTraceRequest\x1a!.jaeger.api_v3.SpansResponseChunk\"\x00\x30\x01\x12U\n\nFindTraces\x12 .jaeger.api_v3.FindTracesRequest\x1a!.jaeger.api_v3.SpansResponseChunk\"\x00\x30\x01\x12V\n\x0bGetServices\x12!.jaeger.api_v3.GetServicesRequest\x1a\".jaeger.api_v3.GetServicesResponse\"\x00\x12\\\n\rGetOperations\x12#.jaeger.api_v3.GetOperationsRequest\x1a$.jaeger.api_v3.GetOperationsResponse\"\x00\x42!\n\x17io.jaegertracing.api_v3Z\x06\x61pi_v3b\x06proto3'
  ,
  dependencies=[opentelemetry_dot_proto_dot_trace_dot_v1_dot_trace__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_GETTRACEREQUEST = _descriptor.Descriptor(
  name='GetTraceRequest',
  full_name='jaeger.api_v3.GetTraceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='jaeger.api_v3.GetTraceRequest.trace_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='jaeger.api_v3.GetTraceRequest.start_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='jaeger.api_v3.GetTraceRequest.end_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=282,
)


_SPANSRESPONSECHUNK = _descriptor.Descriptor(
  name='SpansResponseChunk',
  full_name='jaeger.api_v3.SpansResponseChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_spans', full_name='jaeger.api_v3.SpansResponseChunk.resource_spans', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=373,
)


_TRACEQUERYPARAMETERS_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='jaeger.api_v3.TraceQueryParameters.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='jaeger.api_v3.TraceQueryParameters.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='jaeger.api_v3.TraceQueryParameters.AttributesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=790,
)

_TRACEQUERYPARAMETERS = _descriptor.Descriptor(
  name='TraceQueryParameters',
  full_name='jaeger.api_v3.TraceQueryParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='jaeger.api_v3.TraceQueryParameters.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation_name', full_name='jaeger.api_v3.TraceQueryParameters.operation_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='jaeger.api_v3.TraceQueryParameters.attributes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time_min', full_name='jaeger.api_v3.TraceQueryParameters.start_time_min', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time_max', full_name='jaeger.api_v3.TraceQueryParameters.start_time_max', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration_min', full_name='jaeger.api_v3.TraceQueryParameters.duration_min', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration_max', full_name='jaeger.api_v3.TraceQueryParameters.duration_max', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_traces', full_name='jaeger.api_v3.TraceQueryParameters.num_traces', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TRACEQUERYPARAMETERS_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=376,
  serialized_end=790,
)


_FINDTRACESREQUEST = _descriptor.Descriptor(
  name='FindTracesRequest',
  full_name='jaeger.api_v3.FindTracesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='jaeger.api_v3.FindTracesRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=792,
  serialized_end=863,
)


_GETSERVICESREQUEST = _descriptor.Descriptor(
  name='GetServicesRequest',
  full_name='jaeger.api_v3.GetServicesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=865,
  serialized_end=885,
)


_GETSERVICESRESPONSE = _descriptor.Descriptor(
  name='GetServicesResponse',
  full_name='jaeger.api_v3.GetServicesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='jaeger.api_v3.GetServicesResponse.services', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=926,
)


_GETOPERATIONSREQUEST = _descriptor.Descriptor(
  name='GetOperationsRequest',
  full_name='jaeger.api_v3.GetOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='jaeger.api_v3.GetOperationsRequest.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='span_kind', full_name='jaeger.api_v3.GetOperationsRequest.span_kind', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=928,
  serialized_end=986,
)


_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='jaeger.api_v3.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='jaeger.api_v3.Operation.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='span_kind', full_name='jaeger.api_v3.Operation.span_kind', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=988,
  serialized_end=1032,
)


_GETOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='GetOperationsResponse',
  full_name='jaeger.api_v3.GetOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='jaeger.api_v3.GetOperationsResponse.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1034,
  serialized_end=1103,
)

_GETTRACEREQUEST.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETTRACEREQUEST.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SPANSRESPONSECHUNK.fields_by_name['resource_spans'].message_type = opentelemetry_dot_proto_dot_trace_dot_v1_dot_trace__pb2._RESOURCESPANS
_TRACEQUERYPARAMETERS_ATTRIBUTESENTRY.containing_type = _TRACEQUERYPARAMETERS
_TRACEQUERYPARAMETERS.fields_by_name['attributes'].message_type = _TRACEQUERYPARAMETERS_ATTRIBUTESENTRY
_TRACEQUERYPARAMETERS.fields_by_name['start_time_min'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRACEQUERYPARAMETERS.fields_by_name['start_time_max'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRACEQUERYPARAMETERS.fields_by_name['duration_min'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TRACEQUERYPARAMETERS.fields_by_name['duration_max'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_FINDTRACESREQUEST.fields_by_name['query'].message_type = _TRACEQUERYPARAMETERS
_GETOPERATIONSRESPONSE.fields_by_name['operations'].message_type = _OPERATION
DESCRIPTOR.message_types_by_name['GetTraceRequest'] = _GETTRACEREQUEST
DESCRIPTOR.message_types_by_name['SpansResponseChunk'] = _SPANSRESPONSECHUNK
DESCRIPTOR.message_types_by_name['TraceQueryParameters'] = _TRACEQUERYPARAMETERS
DESCRIPTOR.message_types_by_name['FindTracesRequest'] = _FINDTRACESREQUEST
DESCRIPTOR.message_types_by_name['GetServicesRequest'] = _GETSERVICESREQUEST
DESCRIPTOR.message_types_by_name['GetServicesResponse'] = _GETSERVICESRESPONSE
DESCRIPTOR.message_types_by_name['GetOperationsRequest'] = _GETOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.message_types_by_name['GetOperationsResponse'] = _GETOPERATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTraceRequest = _reflection.GeneratedProtocolMessageType('GetTraceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRACEREQUEST,
  '__module__' : 'api_v3.query_service_pb2'
  # @@protoc_insertion_point(class_scope:jaeger.api_v3.GetTraceRequest)
  })
_sym_db.RegisterMessage(GetTraceRequest)

SpansResponseChunk = _reflection.GeneratedProtocolMessageType('SpansResponseChunk', (_message.Message,), {
  'DESCRIPTOR' : _SPANSRESPONSECHUNK,
  '__module__' : 'api_v3.query_service_pb2'
  # @@protoc_insertion_point(class_scope:jaeger.api_v3.SpansResponseChunk)
  })
_sym_db.RegisterMessage(SpansResponseChunk)

TraceQueryParameters = _reflection.GeneratedProtocolMessageType('TraceQueryParameters', (_message.Message,), {

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRACEQUERYPARAMETERS_ATTRIBUTESENTRY,
    '__module__' : 'api_v3.query_service_pb2'
    # @@protoc_insertion_point(class_scope:jaeger.api_v3.TraceQueryParameters.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _TRACEQUERYPARAMETERS,
  '__module__' : 'api_v3.query_service_pb2'
  # @@protoc_insertion_point(class_scope:jaeger.api_v3.TraceQueryParameters)
  })
_sym_db.RegisterMessage(TraceQueryParameters)
_sym_db.RegisterMessage(TraceQueryParameters.AttributesEntry)

FindTracesRequest = _reflection.GeneratedProtocolMessageType('FindTracesRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDTRACESREQUEST,
  '__module__' : 'api_v3.query_service_pb2'
  # @@protoc_insertion_point(class_scope:jaeger.api_v3.FindTracesRequest)
  })
_sym_db.RegisterMessage(FindTracesRequest)

GetServicesRequest = _reflection.GeneratedProtocolMessageType('GetServicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVICESREQUEST,
  '__module__' : 'api_v3.query_service_pb2'
  # @@protoc_insertion_point(class_scope:jaeger.api_v3.GetServicesRequest)
  })
_sym_db.RegisterMessage(GetServicesRequest)

GetServicesResponse = _reflection.GeneratedProtocolMessageType('GetServicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVICESRESPONSE,
  '__module__' : 'api_v3.query_service_pb2'
  # @@protoc_insertion_point(class_scope:jaeger.api_v3.GetServicesResponse)
  })
_sym_db.RegisterMessage(GetServicesResponse)

GetOperationsRequest = _reflection.GeneratedProtocolMessageType('GetOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOPERATIONSREQUEST,
  '__module__' : 'api_v3.query_service_pb2'
  # @@protoc_insertion_point(class_scope:jaeger.api_v3.GetOperationsRequest)
  })
_sym_db.RegisterMessage(GetOperationsRequest)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'api_v3.query_service_pb2'
  # @@protoc_insertion_point(class_scope:jaeger.api_v3.Operation)
  })
_sym_db.RegisterMessage(Operation)

GetOperationsResponse = _reflection.GeneratedProtocolMessageType('GetOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETOPERATIONSRESPONSE,
  '__module__' : 'api_v3.query_service_pb2'
  # @@protoc_insertion_point(class_scope:jaeger.api_v3.GetOperationsResponse)
  })
_sym_db.RegisterMessage(GetOperationsResponse)


DESCRIPTOR._options = None
_TRACEQUERYPARAMETERS_ATTRIBUTESENTRY._options = None

_QUERYSERVICE = _descriptor.ServiceDescriptor(
  name='QueryService',
  full_name='jaeger.api_v3.QueryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1106,
  serialized_end=1472,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTrace',
    full_name='jaeger.api_v3.QueryService.GetTrace',
    index=0,
    containing_service=None,
    input_type=_GETTRACEREQUEST,
    output_type=_SPANSRESPONSECHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FindTraces',
    full_name='jaeger.api_v3.QueryService.FindTraces',
    index=1,
    containing_service=None,
    input_type=_FINDTRACESREQUEST,
    output_type=_SPANSRESPONSECHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetServices',
    full_name='jaeger.api_v3.QueryService.GetServices',
    index=2,
    containing_service=None,
    input_type=_GETSERVICESREQUEST,
    output_type=_GETSERVICESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetOperations',
    full_name='jaeger.api_v3.QueryService.GetOperations',
    index=3,
    containing_service=None,
    input_type=_GETOPERATIONSREQUEST,
    output_type=_GETOPERATIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERYSERVICE)

DESCRIPTOR.services_by_name['QueryService'] = _QUERYSERVICE

# @@protoc_insertion_point(module_scope)
