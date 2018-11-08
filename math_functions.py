import math

# real_gap debe ser variable opcional, condicionada a preceding_car=True
# quizas iniciarla igual a 1?


def mag(x, y):
    return math.sqrt(math.pow(x, 2.0) + math.pow(y, 2.0))


def estimated_accel(v, dv, real_gap, preceding_car=True, a=0.5, u=16.7, exp=4):
    # u = 60km/h = 16.6...m/s

    def desired_gap(d0=2.0, T=0.8, b=3.0):
        if preceding_car:
            return d0 + (T * v) + (float(v * dv) / (2.0 * math.sqrt(a * b)))
        else:
            return 0.0

    x = math.pow((float(v) / float(u)), exp)
    y = math.pow(desired_gap() / real_gap, 2)

    return a * (1.0 - x - y)


def estimated_nextposition(estimated_accel, posx, posy, vel, timestep=0.1):

    estimated_vel = vel + timestep * estimated_accel
    direction = math.atan(posy / posx)
    estimated_posx = (posx + (estimated_vel * math.cos(direction) * timestep) +
                      ((1.0 / 2.0) * (estimated_accel * math.cos(direction) * (math.pow(timestep, 2.0)))))
    estimated_posy = (posy + (estimated_vel * math.sin(direction) * timestep) +
                      ((1.0 / 2.0) * (estimated_accel * math.sin(direction) * (math.pow(timestep, 2.0)))))
    return (estimated_posx, estimated_posy, estimated_vel)


def error(v, pos, estimated_pos, var_pos=1.2, var_vel=1.2):
    return math.sqrt(math.pow((v - estimated_pos[2]), 2.0)
                     + math.pow((mag(pos[0], pos[1]) - mag(estimated_pos[0], estimated_pos[1])), 2.0))



# calcula la posibilidad del siguiente giro
# recibe, velocidad, posicion (no se usa), vel_actual, pos_actual, prom=0
def probable_turn(vel, pos, vel_actual, pos_actual, prom=0):

    prob_modelos = (0.18, 0.62, 0.2)
    prob_acc_mod1 = (0.59, 0.25, 0.16)
    prob_acc_mod2 = (0.25, 0.5, 0.25)
    prob_acc_mod3 = (0.16, 0.4, 0.44)
    acc=(1.5, 2, 2.5)
    vels=(13.33, 15, 16.67)
    suma = 0.0
    prob_acc_mod = 0.0
    for modelos in range(0, 3):
        for casos in range(0, 3):
            if modelos == 0:
                prob_acc_mod = prob_acc_mod1[casos]
            elif modelos == 1:
                prob_acc_mod = prob_acc_mod2[casos]
            elif modelos == 2:
                prob_acc_mod = prob_acc_mod3[casos]

            estimated_a = estimated_accel(vel, 0.0, 1.0, False, acc[casos], vels[casos])
            estimated_nextpos = estimated_nextposition(
                estimated_a, pos_actual[0], pos_actual[1], vel)
            err = error(vel_actual, pos_actual, estimated_nextpos)
            dens_prob = (1.0 / (2.0 * math.pi * 1.2)) * \
                math.exp((-1.0) * (1.0 / 2.0) * math.pow(err, 2.0))            
            prob_hyp = 0.5 * prob_modelos[modelos] * prob_acc_mod
            num = dens_prob * prob_hyp
            suma = suma + num
    val_1_15 = (dens_prob * 0.5 * prob_modelos[0] * prob_acc_mod1[0]) / suma
    val_2_15 = (dens_prob * 0.5 * prob_modelos[1] * prob_acc_mod2[0]) / suma
    val_3_15 = (dens_prob * 0.5 * prob_modelos[2] * prob_acc_mod3[0]) / suma
    val_2_2 = (dens_prob * 0.5 * prob_modelos[1] * prob_acc_mod2[1]) / suma
    val_3_2 = (dens_prob * 0.5 * prob_modelos[2] * prob_acc_mod3[1]) / suma
    prob_giro = val_1_15 + val_2_15 + val_3_15 + val_2_2 + val_3_2
    if math.fabs(prom-prob_giro)>0.02:
        return (1, prob_giro)
    else:
        return (0, prob_giro)
