Name:           ros-lunar-rc-dynamics-api
Version:        0.6.0
Release:        0%{?dist}
Summary:        ROS rc_dynamics_api package

Group:          Development/Libraries
License:        BSD
URL:            http://rc-visard.com
Source0:        %{name}-%{version}.tar.gz

Requires:       curl
Requires:       libcurl-devel
Requires:       protobuf
Requires:       ros-lunar-catkin
BuildRequires:  cmake
BuildRequires:  curl
BuildRequires:  libcurl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel

%description
The rc_dynamics_api provides an API for easy handling of the dynamic-state data
streams provided by Roboception's stereo camera with self-localization. See http
://rc-visard.com Dynamic-state estimates of the rc_visard relate to its self-
localization and ego-motion estimation. These states refer to rc_visard's
current pose, velocity, or acceleration and are published on demand via several
data streams. For a complete list and descriptions of these dynamics states and
the respective data streams please refer to rc_visard's user manual.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu Apr 19 2018 Felix Ruess <felix.ruess@roboception.de> - 0.6.0-0
- Autogenerated by Bloom

* Tue Feb 27 2018 Felix Ruess <felix.ruess@roboception.de> - 0.5.0-0
- Autogenerated by Bloom

