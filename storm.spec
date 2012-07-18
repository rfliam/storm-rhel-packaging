Name: storm	
Version: 0.7.4
Release: 1%{?dist}
Summary: Storm Complex Event Processing	
Group: Applications/Internet
License: EPLv1
URL: http://storm-project.net
Source: https://github.com/downloads/nathanmarz/storm/storm-%{version}.tgz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: jdk jzmq 	
%description
Storm is a distributed realtime computation system. Similar to how Hadoop provides a set of general primitives for doing batch processing, Storm provides a set of general primitives for doing realtime computation. Storm is simple, can be used with any programming language, is used by many companies, and is a lot of fun to use!

The Rationale page on the wiki explains what Storm is and why it was built. This presentation is also a good introduction to the project.

Storm has a website at storm-project.net. Follow @stormprocessor on Twitter for updates on the project.

%prep
%setup -q

# For now there is no build process, may configure this later so that RPM actually builds. 
# However, as storm build requires leinigen, and leinigen in turne requires
# a ton of shit (namely the open JDK, which I don't want to pull) we will leave this out.
%build

%install
# Clean out any previous builds not on slash (lol)
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

# Copy the storm file to the right places
%{__mkdir_p} %{buildroot}/opt/storm-%{version}
%{__mkdir_p} %{buildroot}/etc/sysconfig
%{__mkdir_p} %{buildroot}/etc/storm/conf.d
%{__mkdir_p} %{buildroot}/etc/init.d
%{__mkdir_p} %{buildroot}/var/log/storm
%{__mkdir_p} %{buildroot}/var/opt/storm
%{__cp} -R * %{buildroot}/opt/storm-%{version}/
%{__ln_s} /opt/storm-%{version} %{buildroot}/opt/storm
%{__cp} sysconfig/storm %{buildroot}/etc/sysconfig/storm
%{__cp} init.d/storm-nimbus init.d/storm-supervisor init.d/storm-ui %{buildroot}/etc/init.d

# Form a list of files for the files directive
echo $(cd %{buildroot} && find . -type f | cut -c 2-) | tr ' ' '\n' > files.txt
# Grab the symlinks too
echo $(cd %{buildroot} && find . -type l | cut -c 2-) | tr ' ' '\n' >> files.txt

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files -f files.txt
%defattr(-,root,root,-)

%changelog
* Mon Jul 16 2012 Richard Fliam <zbobet2012@gmail.com>
- Initial Packaging
