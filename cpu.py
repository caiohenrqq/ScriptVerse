import cpuinfo

# Have the library pick the best method for getting your CPU info
info = cpuinfo.get_cpu_info()

# Or use /proc/cpuinfo
#info = cpuinfo.get_cpu_info_from_proc_cpuinfo()

# Or use the Windows registry
#info = cpuinfo.get_cpu_info_from_registry()

# Or use sysctl
#info = cpuinfo.get_cpu_info_from_sysctl()

# Or use CPU CPUID register
#info = cpuinfo.get_cpu_info_from_cpuid()

# Print some CPU values
print('Vendor ID: {0}'.format(info['vendor_id']))
print('Brand: {0}'.format(info['brand']))
print('Hz Advertised: {0}'.format(info['hz_advertised']))
print('Hz Actual: {0}'.format(info['hz_actual']))
print('Hz Advertised Raw: {0}'.format(info['hz_advertised_raw']))
print('Hz Actual Raw: {0}'.format(info['hz_actual_raw']))
print('Arch: {0}'.format(info['arch']))
print('Bits: {0}'.format(info['bits']))
print('Count: {0}'.format(info['count']))
print('Flags: {0}'.format(', '.join(info['flags'])))