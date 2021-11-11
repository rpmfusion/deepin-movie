%undefine __cmake_in_source_build
%global _lto_cflags %{nil}

Name:           deepin-movie
Version:        5.7.11
Release:        3%{?dist}
Summary:        Deepin movie based on mpv
Summary(zh_CN): 深度影音
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-movie-reborn
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-appdata.xml
Patch0:         fix_linking.patch

BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(mpris-qt5)
BuildRequires:  mpv-libs-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  libappstream-glib
BuildRequires:  gcc
BuildRequires:  desktop-file-utils

Requires:  deepin-qt5integration

%description
Deepin movie for deepin desktop environment.

%description -l zh_CN
深度影音播放器, 后端基于MPV, 支持解码大多数视频格式.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1 -n %{name}-reborn-%{version}
sed -i '/dtk2/s|lib|libexec|' src/CMakeLists.txt
sed -i '/#include <DPalette>/a #include <QPainterPath>' src/widgets/{tip,toolbutton}.h
sed -i 's/Exec=deepin-movie/Exec=env QT_QPA_PLATFORMTHEME=deepin deepin-movie/g' ./%{name}.desktop

%build
%cmake3 -DCMAKE_BUILD_TYPE=Release
%cmake3_build

%install
%cmake3_install
install -Dm644 %SOURCE1 %{buildroot}%{_metainfodir}/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

rm -rf %{buildroot}/%{_datadir}/deepin-manual/

%find_lang %{name} --with-qt

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/libdmr.so.0.1
%{_libdir}/libdmr.so.0.1.0
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/glib-2.0/schemas/com.deepin.%{name}.gschema.xml

%files devel
%{_includedir}/libdmr/
%{_libdir}/pkgconfig/libdmr.pc
%{_libdir}/libdmr.so

%changelog
* Thu Nov 11 2021 Leigh Scott <leigh123linux@gmail.com> - 5.7.11-3
- Rebuilt for new ffmpeg snapshot

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 5.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 23 2021 Leigh Scott <leigh123linux@gmail.com> - 5.7.11-1
- Update to 5.7.11

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.24.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 3.2.24.3-6
- Rebuilt for new ffmpeg snapshot

* Mon Nov 23 2020 Leigh Scott <leigh123linux@gmail.com> - 3.2.24.3-5
- Rebuild for new mpv

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.24.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3.2.24.3-3
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 25 2019 Zamir SUN <zsun@fedoraproject.org> - 3.2.24.3-1
- Update to 3.2.24.3

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 3.2.14-3
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Zamir SUN <zsun@fedoraproject.org> - 3.2.14-1
- Update to 3.2.14
- Add BR gcc

* Sat Oct 27 2018 Zamir SUN <zsun@fedoraproject.org> - 3.2.11-1
- Update to 3.2.11

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 3.2.9-1
- Update to 3.2.9

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 3.2.8-1
- Update to 3.2.8

* Tue Mar 20 2018 mosquito <sensor.wen@gmail.com> - 3.2.3-1
- Update to 3.2.3

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 3.2.0.3-1
- Update to 3.2.0.3

* Wed Jan 10 2018 mosquito <sensor.wen@gmail.com> - 3.2.0.2-1
- Update to 3.2.0.2

* Thu Dec 28 2017 Zamir SUN <sztsian@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Wed Dec 20 2017 mosquito <sensor.wen@gmail.com> - 3.1.1-1
- Update to 3.1.1

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 2.9.96-1
- Update to 2.9.96

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 2.9.94-1
- Update to 2.9.94

* Fri Oct 13 2017 mosquito <sensor.wen@gmail.com> - 2.9.16-1
- Update to 2.9.16

* Thu Sep 21 2017 mosquito <sensor.wen@gmail.com> - 2.9.12-1
- Update to 2.9.12

* Thu Aug 24 2017 mosquito <sensor.wen@gmail.com> - 2.9.10-1
- Update to 2.9.10

* Sun Aug 06 2017 Zamir SUN <sztsian@gmail.com> - 2.2.14-2
- Remove group tag
- Fix rpmlint shebang error

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 2.2.14-1.git69123ed
- Update to 2.2.14

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 2.2.13-1.gita1ba8c3
- Update to 2.2.13

* Sat Jan 28 2017 mosquito <sensor.wen@gmail.com> - 2.2.11-2.git7896696
- Fix cannot register existing type 'GdkDisplayManager'

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 2.2.11-1.git7896696
- Update to 2.2.11

* Thu Jul 16 2015 mosquito <sensor.wen@gmail.com> - 2.2.2-2.git53adfc6
- python-peewee(>=2.3.0,<=2.4.4)
- remove some depends

* Sat Jul  4 2015 mosquito <sensor.wen@gmail.com> - 2.2.2-1.git53adfc6
- Initial build
