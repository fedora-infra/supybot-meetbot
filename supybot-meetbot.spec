%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           supybot-meetbot
Version:        0.1.4
Release:        15%{?dist}
Summary:        Plugin for Supybot for handling IRC meetings

Group:          Applications/Internet
License:        BSD
URL:            http://wiki.debian.org/MeetBot
Source0:        http://code.zgib.net/tar//MeetBot-%{version}.tar.gz
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

* Sun Jan 05 2014 Kevin Fenzi <kevin@scrye.com> 0.1.4-12
- Add patch from Michael Scherer to show what undo undid. 

* Wed May 15 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1.4-10
- Fix for traceback if meeting names contain non-ascii chars

* Fri Sep 11 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.4-1
- Update to 0.1.4 release. 