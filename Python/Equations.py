# The file with all of the equations
import math

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
	Reynolds_l= G_l*D/mu_f
	return Reynolds_l
	
def Re_go(G_m, mu_g, pipe_diameter):
	Reynolds_go = G_m*D/mu_g
	return Reynolds_go;
	
def Re_g(G_g, mu_g, pipe_diameter):
	Re_g = G_g*D/mu_g
	return Re_g;
	
def f_lo_mc(G_m, mu_g, pipe_diameter):
	f_lo_mcadams = 0.184*Re_lo**(-0.2)
	return f_lo_mcadams;
	
def rho_m_HEM(m_dot_g, m_dot_f, rho_f, rho_g):
	rho_m_HEM = 1/((x/rho_g)+((1-x)/rho_f))
	return rho_m_HEM;
	
def x(m_dot_g, m_dot_f):
	quality = m_dot_g/(m_dot_g+m_dot_f)
	return quality;

# HEM Correlation
def dp_dz_HEM(G_m, mu_g, m_dot_g, m_dot_f, rho_f, rho_g, pipe_diameter):
	dp_dz_HEM = -f_lo_mc*G_m**2/(2*D*rho_m_HEM)
	return dp_dz_HEM;
	
# Lockheart Martinelli Corellation
def X_tt_squared(mu_f,mu_g,m_dot_g, m_dot_f, rho_g, rho_f):
	X_tt_squared = (mu_f/mu_g)**0.2*((1-x)/x)**1.8(rho_g/rho_f)
	return X_tt_squared;
	
def phi_l_squared(mu_f,mu_g,m_dot_g, m_dot_f, rho_g, rho_f):
	phi_l_squared = 1+(20/X_tt_squared**(0.5))+(1/X_tt_squared)
	return phi_l_squared;
	
def phi_lo_squared_LM(mu_f,mu_g,m_dot_g, m_dot_f, rho_g, rho_f):
	phi_lo_squared = phi_l_squared*(1-x)**(1.8)
	return phi_lo_squared;
	
def dp_dz_LM(mu_f,mu_g,m_dot_g, m_dot_f, rho_g, rho_f, G_m, pipe_diameter):
	dp_dz_LM = -phi_lo_squared_LM*f_lo_mc*G_m**2/(2*D*rho_f)
	return dp_dz_LM;
	
# Friedal Correlation 
def F(m_dot_g, m_dot_f):
	F = x**0.78*(1-x)**0.224
	return F;
	
def H(rho_f, rho_g, mu_g, mu_f):
	H = (rho_f/rho_g)**0.91*(mu_g/mu_f)**0.19*(1-(mu_g/mu_f))**0.7
	return H; 
	
def Fr(G_m, g, m_dot_g, m_dot_f, rho_f, rho_g, pipe_diameter):
	Fr = G_m**2/(g*D*rho_m_HEM**2)
	return Fr;
	
def We(G_m, sigma, m_dot_g, m_dot_f, rho_f, rho_g, pipe_diameter):
	We = G_m**2*D/(sigma*rho_m_HEM)
	return We;
	
def f_go_fri(G_m, mu_f, pipe_diameter):
	f_go_friedal = (0.86859*ln(Re_go/(1.964*ln(Re_go)-3.8215)))**(-2)
	return f_go_friedal;
	
def f_lo_fri(G_m, mu_f, pipe_diameter):
	f_lo_friedal = (0.86859*ln(Re_lo/(1.964*ln(Re_lo)-3.8215)))**(-2)
	return f_lo_friedal;
	
def E(m_dot_g, m_dot_f, rho_f, G_m, mu_f, rho_g, mu_g, pipe_diameter):
	E = (1-x)**2+x**2*rho_f*f_lo_fri/(rho_g*f_go_fri)
	return E;
	
def phi_lo_squared_fri(m_dot_g, m_dot_f, rho_f, G_m, mu_f, rho_g, mu_g, sigma, pipe_diameter):
	phi_lo_squared_friedal = E+(3.24*F*H/(Fr**0.0454*We**0.035))
	return phi_lo_squared_friedal;
	
def dp_dz_fri(m_dot_g, m_dot_f, rho_f, G_m, mu_f, rho_g, mu_g, sigma, pipe_diameter):
	dp_dz_friedal = -f_lo_fri*phi_lo_squared_fri*G_m**2/(2*D*rho_m_HEM)
	return dp_dz_friedal
	
# n=126

# X_tt_squared_2 = (mu_f/mu_g)^0.2*((1-x)/x)^1.8(rho_g/rho_f)
# phi_l_squared_2 = 1+(C/X_tt_squared^(0.5))+(1/X_tt_squared)
# phi_lo_squared_LM_2 = phi_l_squared*(1-x)^(1.8)
# -dp_dz_LM_2 = phi_lo_squared_LM*f_lo_mc*G_m^2/(2*D*rho_f)

# f_lo_3 = C_1*Re_lo^c_2
# f_l_3 = C_1*Re_l^c_2
# f_g_3 = C_1*Re_g^c_2

# dp_dz_fric_lo_3 = f_lo*G_m*U_sg/D
# dp_dz_fric_l_3 = f_l*G_m*U_sg/D
# dp_dz_fric_g_3 = f_g*G_m*U_sg/D
