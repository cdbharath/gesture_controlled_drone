# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ardrone_autonomy/navdata_vision_detect.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ardrone_autonomy.msg
import std_msgs.msg

class navdata_vision_detect(genpy.Message):
  _md5sum = "ab5f6b8c66aead58358d45a7c2dce7f6"
  _type = "ardrone_autonomy/navdata_vision_detect"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
float64 drone_time
uint16 tag
uint16 size
uint32 nb_detected
uint32[] type
uint32[] xc
uint32[] yc
uint32[] width
uint32[] height
uint32[] dist
float32[] orientation_angle
matrix33[] rotation
vector31[] translation
uint32[] camera_source

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: ardrone_autonomy/matrix33
float32 m11
float32 m12
float32 m13
float32 m21
float32 m22
float32 m23
float32 m31
float32 m32
float32 m33
================================================================================
MSG: ardrone_autonomy/vector31
float32 x
float32 y
float32 z"""
  __slots__ = ['header','drone_time','tag','size','nb_detected','type','xc','yc','width','height','dist','orientation_angle','rotation','translation','camera_source']
  _slot_types = ['std_msgs/Header','float64','uint16','uint16','uint32','uint32[]','uint32[]','uint32[]','uint32[]','uint32[]','uint32[]','float32[]','ardrone_autonomy/matrix33[]','ardrone_autonomy/vector31[]','uint32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,drone_time,tag,size,nb_detected,type,xc,yc,width,height,dist,orientation_angle,rotation,translation,camera_source

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(navdata_vision_detect, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.drone_time is None:
        self.drone_time = 0.
      if self.tag is None:
        self.tag = 0
      if self.size is None:
        self.size = 0
      if self.nb_detected is None:
        self.nb_detected = 0
      if self.type is None:
        self.type = []
      if self.xc is None:
        self.xc = []
      if self.yc is None:
        self.yc = []
      if self.width is None:
        self.width = []
      if self.height is None:
        self.height = []
      if self.dist is None:
        self.dist = []
      if self.orientation_angle is None:
        self.orientation_angle = []
      if self.rotation is None:
        self.rotation = []
      if self.translation is None:
        self.translation = []
      if self.camera_source is None:
        self.camera_source = []
    else:
      self.header = std_msgs.msg.Header()
      self.drone_time = 0.
      self.tag = 0
      self.size = 0
      self.nb_detected = 0
      self.type = []
      self.xc = []
      self.yc = []
      self.width = []
      self.height = []
      self.dist = []
      self.orientation_angle = []
      self.rotation = []
      self.translation = []
      self.camera_source = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_d2HI().pack(_x.drone_time, _x.tag, _x.size, _x.nb_detected))
      length = len(self.type)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.type))
      length = len(self.xc)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.xc))
      length = len(self.yc)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.yc))
      length = len(self.width)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.width))
      length = len(self.height)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.height))
      length = len(self.dist)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.dist))
      length = len(self.orientation_angle)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.orientation_angle))
      length = len(self.rotation)
      buff.write(_struct_I.pack(length))
      for val1 in self.rotation:
        _x = val1
        buff.write(_get_struct_9f().pack(_x.m11, _x.m12, _x.m13, _x.m21, _x.m22, _x.m23, _x.m31, _x.m32, _x.m33))
      length = len(self.translation)
      buff.write(_struct_I.pack(length))
      for val1 in self.translation:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      length = len(self.camera_source)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.camera_source))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.rotation is None:
        self.rotation = None
      if self.translation is None:
        self.translation = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.drone_time, _x.tag, _x.size, _x.nb_detected,) = _get_struct_d2HI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.type = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.xc = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.yc = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.width = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.height = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.dist = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.orientation_angle = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.rotation = []
      for i in range(0, length):
        val1 = ardrone_autonomy.msg.matrix33()
        _x = val1
        start = end
        end += 36
        (_x.m11, _x.m12, _x.m13, _x.m21, _x.m22, _x.m23, _x.m31, _x.m32, _x.m33,) = _get_struct_9f().unpack(str[start:end])
        self.rotation.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.translation = []
      for i in range(0, length):
        val1 = ardrone_autonomy.msg.vector31()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.translation.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.camera_source = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_d2HI().pack(_x.drone_time, _x.tag, _x.size, _x.nb_detected))
      length = len(self.type)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.type.tostring())
      length = len(self.xc)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.xc.tostring())
      length = len(self.yc)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.yc.tostring())
      length = len(self.width)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.width.tostring())
      length = len(self.height)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.height.tostring())
      length = len(self.dist)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.dist.tostring())
      length = len(self.orientation_angle)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.orientation_angle.tostring())
      length = len(self.rotation)
      buff.write(_struct_I.pack(length))
      for val1 in self.rotation:
        _x = val1
        buff.write(_get_struct_9f().pack(_x.m11, _x.m12, _x.m13, _x.m21, _x.m22, _x.m23, _x.m31, _x.m32, _x.m33))
      length = len(self.translation)
      buff.write(_struct_I.pack(length))
      for val1 in self.translation:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      length = len(self.camera_source)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.camera_source.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.rotation is None:
        self.rotation = None
      if self.translation is None:
        self.translation = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.drone_time, _x.tag, _x.size, _x.nb_detected,) = _get_struct_d2HI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.type = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.xc = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.yc = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.width = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.height = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.dist = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.orientation_angle = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.rotation = []
      for i in range(0, length):
        val1 = ardrone_autonomy.msg.matrix33()
        _x = val1
        start = end
        end += 36
        (_x.m11, _x.m12, _x.m13, _x.m21, _x.m22, _x.m23, _x.m31, _x.m32, _x.m33,) = _get_struct_9f().unpack(str[start:end])
        self.rotation.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.translation = []
      for i in range(0, length):
        val1 = ardrone_autonomy.msg.vector31()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.translation.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.camera_source = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_d2HI = None
def _get_struct_d2HI():
    global _struct_d2HI
    if _struct_d2HI is None:
        _struct_d2HI = struct.Struct("<d2HI")
    return _struct_d2HI
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_9f = None
def _get_struct_9f():
    global _struct_9f
    if _struct_9f is None:
        _struct_9f = struct.Struct("<9f")
    return _struct_9f
