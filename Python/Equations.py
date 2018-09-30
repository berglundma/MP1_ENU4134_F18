# The file with all of the equations
import math

g = 9.81
sigma = 0.07407

def A(pipe_diameter):
    area = ((math.pi*(pipe_diameter**2))/4)
    return area;

def G_m(m_dot_f, m_dot_g, pipe_diameter):
    gm=(m_dot_g/A(pipe_diameter)) + (m_dot_f/A(pipe_diameter))
    return gm;

def G_l(m_dot_f, pipe_diameter):
	G_l = (m_dot_f/A(pipe_diameter))
	return G_l;

def G_g(m_dot_g, pipe_diameter):
	G_g = (m_dot_g/A(pipe_diameter))
	return G_g;

def U_sg(m_dot_g, rho_g, pipe_diameter):
	U_sg = m_dot_g/(A(pipe_diameter)*rho_g)
	return U_sg;

def Re_lo(G_m, mu_f, pipe_diameter):
	Reynolds_lo = G_m*pipe_diameter/mu_f
	return Reynolds_lo;

def Re_l(G_l, mu_f, pipe_diameter):
	Reynolds_l= G_l*pipe_diameter/mu_f
	return Reynolds_l

def Re_go(G_m, mu_g, pipe_diameter):
	Reynolds_go = G_m*pipe_diameter/mu_g
	return Reynolds_go;

def Re_g(G_g, mu_g, pipe_diameter):
	Re_g = G_g*pipe_diameter/mu_g
	return Re_g;

def f_lo_mc(G_m, mu_f, pipe_diameter):
	Re = Re_lo(G_m, mu_f, pipe_diameter)
	f_lo_mcadams = 0.184*Re**(-0.2)
	return f_lo_mcadams;

def x(m_dot_g, m_dot_f):
	quality = m_dot_g/(m_dot_g+m_dot_f)
	return quality;

def rho_m_HEM(m_dot_g, m_dot_f, rho_f, rho_g):
	rho_m_HEM = 1/((x(m_dot_g, m_dot_f)/rho_g)+((1-x(m_dot_g, m_dot_g))/rho_f))
	return rho_m_HEM;

# HEM Correlation
def dp_dz_HEM(G_m, mu_f, m_dot_g, m_dot_f, rho_f, rho_g, pipe_diameter):
    f_lo_mcadams = f_lo_mc(G_m, mu_f, pipe_diameter)
    rho_m = rho_m_HEM(m_dot_g, m_dot_f, rho_f, rho_g)
    dp_dz_HEM = -((f_lo_mcadams*G_m**2)/(2*pipe_diameter*rho_m))
    return dp_dz_HEM;

# Lockheart Martinelli Corellation
def X_tt_squared(mu_f, mu_g, m_dot_g, m_dot_f, rho_g, rho_f):
	X_tt_squared = (mu_f/mu_g)**0.2*((1-x(m_dot_g, m_dot_f))/x(m_dot_g, m_dot_f))**1.8*(rho_g/rho_f)
	return X_tt_squared;

def phi_l_squared(mu_f,mu_g,m_dot_g, m_dot_f, rho_g, rho_f):
	X_t = X_tt_squared(mu_f,mu_g,m_dot_g, m_dot_f, rho_g, rho_f)
	phi_l_squared = 1+(20/X_t**(0.5))+(1/X_t)
	return phi_l_squared;

def phi_lo_squared_LM(mu_f, mu_g, m_dot_g, m_dot_f, rho_g, rho_f):
	phi_l = phi_l_squared(mu_f, mu_g, m_dot_g, m_dot_f, rho_g, rho_f)
	phi_lo_squared = phi_l*(1-x(m_dot_g, m_dot_f)**(1.8))
	return phi_lo_squared;

def dp_dz_LM(mu_f,mu_g,m_dot_g, m_dot_f, rho_g, rho_f, G_m, pipe_diameter):
	phi_lo = phi_lo_squared_LM(mu_f,mu_g,m_dot_g, m_dot_f, rho_g, rho_f)
	f_lo_mcadams = f_lo_mc(G_m, mu_f, pipe_diameter)
	dp_dz_LM = -(phi_lo*f_lo_mcadams*G_m**2/(2*pipe_diameter*rho_f))
	return dp_dz_LM;

# Friedal Correlation
def F(m_dot_g, m_dot_f):
	F = x(m_dot_g, m_dot_f)**0.78*(1-x(m_dot_g, m_dot_f))**0.224
	return F;

def H(rho_f, rho_g, mu_g, mu_f):
	H = (rho_f/rho_g)**0.91*(mu_g/mu_f)**0.19*(1-(mu_g/mu_f))**0.7
	return H;

def Fr(G_m, m_dot_g, m_dot_f, rho_f, rho_g, pipe_diameter):
    rho_m_H = rho_m_HEM(m_dot_g, m_dot_f, rho_f, rho_g)
    Fr = G_m**2/(g*pipe_diameter*rho_m_H**2)
    return Fr;

def We(G_m, sigma, m_dot_g, m_dot_f, rho_f, rho_g, pipe_diameter):
	rho_m_H = rho_m_HEM(m_dot_g, m_dot_f, rho_f, rho_g)
	We = (G_m**2*pipe_diameter)/(sigma*rho_m_H)
	return We;

def f_go_fri(G_m, mu_g, pipe_diameter):
	Re_go_temp = Re_go(G_m, mu_g, pipe_diameter)
	f_go_friedal = (0.86859*math.log(Re_go_temp/(1.964*math.log(Re_go_temp)-3.8215)))**(-2)
	return f_go_friedal;

def f_lo_fri(G_m, mu_f, pipe_diameter):
	Re_lo_temp = Re_lo(G_m, mu_f, pipe_diameter)
	f_lo_friedal = (0.86859*math.log(Re_lo_temp/(1.964*math.log(Re_lo_temp)-3.8215)))**(-2)
	return f_lo_friedal;

def E(m_dot_g, m_dot_f, rho_f, G_m, mu_f, rho_g, mu_g, pipe_diameter):
	f_lo_fri_temp = f_lo_fri(G_m, mu_f, pipe_diameter)
	f_go_fri_temp = f_go_fri(G_m, mu_g, pipe_diameter)
	E = (1-x(m_dot_g, m_dot_f))**2+x(m_dot_g, m_dot_f)**2*rho_f*f_go_fri_temp/(rho_g*f_lo_fri_temp)
	return E;

def phi_lo_squared_fri(m_dot_g, m_dot_f, rho_f, G_m, mu_f, rho_g, mu_g, sigma, pipe_diameter):
	E_temp = E(m_dot_g, m_dot_f, rho_f, G_m, mu_f, rho_g, mu_g, pipe_diameter)
	F_temp = F(m_dot_g, m_dot_f)
	H_temp = H(rho_f, rho_g, mu_g, mu_f)
	Fr_temp = Fr(G_m, m_dot_g, m_dot_f, rho_f, rho_g, pipe_diameter)
	We_temp = We(G_m, sigma, m_dot_g, m_dot_f, rho_f, rho_g, pipe_diameter)
	phi_lo_squared_friedal = E_temp+(3.24*F_temp*H_temp/(Fr_temp**0.0454*We_temp**0.035))
	return phi_lo_squared_friedal;

def dp_dz_fri(m_dot_g, m_dot_f, rho_f, G_m, mu_f, rho_g, mu_g, sigma, pipe_diameter):
	phi_lo_squared_fri_temp = phi_lo_squared_fri(m_dot_g, m_dot_f, rho_f, G_m, mu_f, rho_g, mu_g, sigma, pipe_diameter)
	f_lo_fri_temp = f_lo_fri(G_m, mu_f, pipe_diameter)
	dp_dz_friedal = -(f_lo_fri_temp*phi_lo_squared_fri_temp*G_m**2/(2*pipe_diameter*rho_f))
	return dp_dz_friedal;

####### PART 2 #######
def X_tt_squared_2(mu_f, mu_g, m_dot_f, m_dot_g, rho_f, rho_g):
	X_tt_squared_2 = (mu_f/mu_g)**0.2*((1-x(m_dot_g, m_dot_f))/x(m_dot_g, m_dot_f))**1.8*(rho_g/rho_f)
	return X_tt_squared_2;

def phi_l_squared_2(mu_f, mu_g, m_dot_f, m_dot_g, rho_f, rho_g, C):
	X_tt_squared = X_tt_squared_2(mu_f, mu_g, m_dot_f, m_dot_g, rho_f, rho_g)
	phi_l_squared_2 = 1+(C/X_tt_squared**(0.5))+(1/X_tt_squared)
	return phi_l_squared_2;

def phi_lo_squared_2(mu_f, mu_g, m_dot_f, m_dot_g, rho_f, rho_g, C):
	phi_l_squared = phi_l_squared_2(mu_f, mu_g, m_dot_f, m_dot_g, rho_f, rho_g, C)
	phi_lo_squared_2 = phi_l_squared*(1-x(m_dot_g, m_dot_f))**(1.8)
	return phi_lo_squared_2;

def dp_dz_LM_2(mu_f, mu_g, m_dot_f, m_dot_g, rho_f, rho_g, G_m, pipe_diameter, C):
	phi_lo_squared = phi_lo_squared_2(mu_f, mu_g, m_dot_f, m_dot_g, rho_f, rho_g, C)
	f_lo_mcadams = f_lo_mc(G_m, mu_f, pipe_diameter)
	dp_dz_LM_2 = -(phi_lo_squared*f_lo_mcadams*G_m**2)/(2*pipe_diameter*rho_f)
	return dp_dz_LM_2;

####### PART 3 #######
def dp_dz_fric_lo_3(G_m, mu_f, m_dot_g, rho_g, pipe_diameter):
	Re_lo_temp = Re_lo(G_m, mu_f, pipe_diameter)
	U_sg_temp = U_sg(m_dot_g, rho_g, pipe_diameter)
	dp_dz_fric_lo_3 = (C_1*Re_lo_temp^C_2)*G_m*U_sg_temp/pipe_diameter
	return dp_dz_fric_lo_3

def dp_dz_fric_l_3(G_l, mu_f, m_dot_g, rho_g, pipe_diameter):
	Re_l_temp = Re_l(G_l, mu_f, pipe_diameter)
	U_sg_temp = U_sg(m_dot_g, rho_g, pipe_diameter)
	dp_dz_fric_l_3 = (C_1*Re_l_temp^C_2)*G_m*U_sg_temp/pipe_diameter
	return dp_dz_fric_l_3

def dp_dz_fric_g_3(G_g, mu_g, m_dot_g, rho_g, pipe_diameter):
	Re_g_temp = Re_g(G_g, mu_g, pipe_diameter)
	U_sg_temp = U_sg(m_dot_g, rho_g, pipe_diameter)
	dp_dz_fric_g_3 = (C_1*Re_g_temp^C_2)*G_m*U_sg_temp/pipe_diameter
	return dp_dz_fric_g_3
