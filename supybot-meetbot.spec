%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           supybot-meetbot
Version:        0.1.4
Release:        15%{?dist}
Summary:        Plugin for Supybot for handling IRC meetings

Group:          Applications/Internet
License:        BSD
URL:            http://wiki.debian.org/MeetBot
Source0:        http://code.zgib.net/tar//MeetBot-%{version}.tar.gz
Patch1:         meetbot-show_string_on_remove.patch
Patch2:         meetbot-force-meetingname.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       /usr/bin/supybot
Requires:       python-pygments
Requires:       python-docutils
Requires:       python-kitchen

BuildArch:      noarch
BuildRequires:  python

%description
MeatBot is designed to assist in running meetings, taking notes, and so on. 
It is in pure python, as a plugin to supybot. However, there is a clear 
distinction between meeting-code and IRC-code, so it should be relatively 
easy to port to other bots. It is under the supybot license (3-clause BSD).

%prep
%setup -q -n MeetBot-%{version}
%patch1
%patch2 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT/%{python_sitelib}/supybot/plugins/MeetBot
install -pm 644 *.py $RPM_BUILD_ROOT/%{python_sitelib}/supybot/plugins/MeetBot
install -pm 644 *.css $RPM_BUILD_ROOT/%{python_sitelib}/supybot/plugins/MeetBot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt doc/Manual.txt doc/meetingLocalConfig-example.py
%{python_sitelib}/supybot/plugins/MeetBot

%changelog
* Wed Nov 18 2015 Kevin Fenzi <kevin@scrye.com> - 0.1.4-15
- Add patch to force meeting name on start. Fixes bug #1283357

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 05 2014 Kevin Fenzi <kevin@scrye.com> 0.1.4-12
- Add patch from Michael Scherer to show what undo undid. 

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 15 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1.4-10
- Fix for traceback if meeting names contain non-ascii chars

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 18 2011 Dave Riches <david.r@ultracar.co.uk> - 0.1.4-6
- added requires /usr/bin/supybot to fix dependency issue

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Sep 11 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.4-3
- Add default css files. 

* Fri Sep 11 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.4-2
- Fix url

* Fri Sep 11 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.4-1
- Update to 0.1.4 release. 

* Sun Aug 23 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.3-1
- Update to 0.1.3 release. 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.2-1
- Update to 0.1.2 release. 

* Tue Jul 07 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.1-2
- Fix install location to be the correct name. 
- Add additional doc files

* Mon Jul 06 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.1-1
- Upgrade to 0.1.1 version

* Sun Jun 14 2009 Kevin Fenzi <kevin@tummy.com> - 0-0.1.20090614darcs
- Initial version for fedora review